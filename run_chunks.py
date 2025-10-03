import json
import subprocess

# Load JSON file
with open("/content/F5-TTS/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Common CLI options

base_cmd = [
    "f5-tts_infer-cli",
    "--model", "F5TTS_v1_Base",
    "--ref_audio", "/content/F5-TTS/1003.WAV",
    "--ref_text", "I was never meant to know what it feels like to be prey, not in this manner not as something to be savored"
]

# Run for each chunk
for chunk in chunks:
    chunk_id = chunk["id"]
    script = chunk["script"]
    output_file = f"result_{chunk_id}.wav"

    cmd = base_cmd + ["--gen_text", script, "-w", output_file]

    print(f"Running chunk {chunk_id} -> {output_file}")
    subprocess.run(cmd, check=True)
