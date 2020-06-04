import argparse
import os
def main():
   
    prog = "torch-model-archiver "
    model_name_arg = "--model-name bert"
    model_dir = "model_logs"
    serialized_file_arg = "--serialized-file "+ os.path.join(model_dir, "0_BERT/bert_pytorch_model.bin")

    extra_files = []
    for file in os.listdir(model_dir):
        if os.path.isdir(os.path.join(model_dir, file)):
            for f in os.listdir(os.path.join(model_dir, file)):
                extra_files.append(os.path.join(model_dir, file, f))
                # extra_files.append(os.path.join(model_dir, file, f))

        else:
            extra_files.append(os.path.join(model_dir, file))
    version_arg = "--version 0.2.6"
    extra_files_arg = "--extra-files \""+",".join(extra_files)+"\""
    handler_arg ="--handler handler.py"
    cmd_args = [model_name_arg, version_arg, serialized_file_arg, extra_files_arg, handler_arg]
    cmd = prog+ " ".join(cmd_args)
    with open("archive-command.sh", "w+") as output_file:
        output_file.write(cmd+"\n")

if __name__ == '__main__':
    
    main()
    