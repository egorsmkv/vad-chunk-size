import torch
import sphn

from vad import load_vad_model, merge_chunks

# device = torch.device("cuda:0")
device = torch.device("cpu")

chunk_size = 30
default_vad_options = {"vad_onset": 0.500, "vad_offset": 0.363}

vad_model = load_vad_model(
    "models/whisperx-vad-segmentation.bin", device, **default_vad_options
)

audio, sr = sphn.read("file.wav")

vad_segments = vad_model({"waveform": torch.tensor(audio), "sample_rate": sr})

vad_segments = merge_chunks(
    vad_segments,
    chunk_size,
    onset=default_vad_options["vad_onset"],
    offset=default_vad_options["vad_offset"],
)
# extract the segments to files
audio_reader = sphn.FileReader("file.wav")

for idx, row in enumerate(vad_segments):
    print(row)

    seconds = row["end"] - row["start"]
    audio_data, _ = audio_reader.decode_with_padding(
        start_sec=row["start"], duration_sec=seconds
    )

    sphn.write_wav(f"segments/{idx}.wav", audio_data[0], 16_000)
