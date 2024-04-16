from openai_controller import gen_data , gen_instructions
import gradio as gr
import os

def generate_instructions(sample_data):
  # print("SEED : ",instruct)
  with open(os.path.join('data', sample_data.name), 'rb') as f:
            file_content = f.read()
            # print(type(file_content))
            file_path = "my_file.txt"
            try:
                with open('data.txt', 'w') as f:
                  # Write the content to the file
                  content_str = file_content.decode('utf-8')
                  result = gen_instructions(content_str)
                  f.write(content_str)
                  print("File content successfully read.")
            except UnicodeDecodeError as e:
                print(f"Error reading file: {e}")
                # Handle the error (e.g., replace invalid characters with a placeholder)
                content = file_content.decode("utf-8", errors="replace")
                result = gen_instructions(content)
                print("File content read with invalid characters replaced.")
            
#   result = "Please upload a file containing the data you want to generate instructions for."
  return result 


def generate_synthetic_data(instruct,sample_data):
  with open(os.path.join('data', sample_data.name), 'rb') as f:
    file_content = f.read()
    # print(type(file_content))
    try:
      with open('data.txt', 'w') as f:
         # Write the content to the file
         content_str = file_content.decode('utf-8')
        # results = gd(instructions,content_str)
         result = gen_data(instruct,content_str)
         f.write(content_str)
         print("File content successfully read.")
    except UnicodeDecodeError as e:
      print(f"Error reading file: {e}")
      # Handle the error (e.g., replace invalid characters with a placeholder)
      content = file_content.decode("utf-8", errors="replace")
      result = gen_data(instruct,content)
      print("File content read with invalid characters replaced.")
  return result


with gr.Blocks() as demo:
   with gr.Row():
       with gr.Column():
           Instructions = gr.Text(label="Input Instructions")
           file_input = gr.File(label="Upload Sample Data")
       with gr.Column():
           Instruct = gr.Text(label="Generated Instructions")
           Data = gr.Text(label="Generated Synthetic Data")
   btn1 = gr.Button("Generate Instructions")
   btn1.click(generate_instructions,inputs=[file_input], outputs=[Instruct])
   btn2 = gr.Button("Generate Synthetic Data")
   btn2.click(generate_synthetic_data, inputs=[Instructions,file_input], outputs=[Data])
   gr.Examples(["Presenter : Abhishek Pahuja","Contact :abhishek.pahuja@cognizant.com"], inputs=[Instruct])

demo.launch(debug=True)
