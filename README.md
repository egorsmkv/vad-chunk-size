# VAD with `chunk_size`

1. Download the VAD model:

```
mkdir models

wget -O "models/whisperx-vad-segmentation.bin" "https://whisperx.s3.eu-west-2.amazonaws.com/model_weights/segmentation/0b5b3216d60a2d32fc086b47ea8c67589aaeb26b7e07fcbe620d6d0b83e209ea/pytorch_model.bin"
```

2. Place an `file.wav` file.

3. Run:

```
python run_vad.py
```
