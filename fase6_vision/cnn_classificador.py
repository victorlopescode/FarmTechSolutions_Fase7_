import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator # pyright: ignore[reportMissingImports]
from tensorflow.keras.models import Sequential # pyright: ignore[reportMissingImports]
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout # pyright: ignore[reportMissingImports]
from tensorflow.keras.optimizers import Adam # pyright: ignore[reportMissingImports]


def treinar_cnn(
    pasta_base="dataset",
    epochs=20,
    img_size=(150, 150)
):
    # Gera treino e validação a partir da MESMA pasta base
    datagen = ImageDataGenerator(
        rescale=1.0 / 255,
        validation_split=0.2  # 20% das imagens vão pra validação
    )

    train_gen = datagen.flow_from_directory(
        pasta_base,
        target_size=img_size,
        batch_size=32,
        class_mode="binary",
        subset="training"
    )

    val_gen = datagen.flow_from_directory(
        pasta_base,
        target_size=img_size,
        batch_size=32,
        class_mode="binary",
        subset="validation"
    )

    model = Sequential([
        Conv2D(32, (3, 3), activation="relu", input_shape=(*img_size, 3)),
        MaxPooling2D(2, 2),

        Conv2D(64, (3, 3), activation="relu"),
        MaxPooling2D(2, 2),

        Conv2D(128, (3, 3), activation="relu"),
        MaxPooling2D(2, 2),

        Flatten(),
        Dense(128, activation="relu"),
        Dropout(0.3),
        Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer=Adam(learning_rate=0.0005),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    history = model.fit(
        train_gen,
        validation_data=val_gen,
        epochs=epochs
    )

    model.save("modelo_cnn_pragas.h5")
    print("Modelo salvo em modelo_cnn_pragas.h5")
    print("Classes mapeadas:", train_gen.class_indices)
    return model, history