from webscout.Local.utils import download_model
from webscout.Local.model import Model
from webscout.Local.thread import Thread
from webscout.Local import formats

def run_local_llm(repo_id, filename):
    model_path = download_model(repo_id, filename)
    model = Model(model_path, n_gpu_layers=4)
    thread = Thread(model, formats.phi3)
    thread.interact()

def main():
    repo_id = "microsoft/Phi-3-mini-4k-instruct-gguf"
    filename = "Phi-3-mini-4k-instruct-q4.gguf"
    run_local_llm(repo_id, filename)

if __name__ == "__main__":
    main()
