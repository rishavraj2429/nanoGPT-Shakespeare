
import streamlit as st
import subprocess
import sys

st.title("nanoGPT Shakespeare Generator")
st.write("Generate Shakespeare-style text using your trained model.")

start_text = st.text_input("Starting text", "ROMEO:")
num_samples = st.slider("Number of samples", 1, 5, 1)
max_tokens = st.slider("Max new tokens", 100, 700, 300)

if st.button("Generate Text"):
    command = [
        sys.executable, "sample.py",
        "--out_dir=out-shakespeare-char",
        "--device=cpu",
        f"--start={start_text}",
        f"--num_samples={num_samples}",
        f"--max_new_tokens={max_tokens}"
    ]

    with st.spinner("Generating text..."):
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=300
        )

    if result.returncode == 0:
        output = result.stdout
        if "Loading meta" in output:
            output = output.split("Loading meta", 1)[0] + output.split("\n", 1)[-1]
        st.text_area("Generated output", output, height=400)
    else:
        st.error(result.stderr or "Generation failed.")
