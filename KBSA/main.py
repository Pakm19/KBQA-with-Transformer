from gg_search import GoogleSearch
from relevance_ranking import rel_ranking
import gradio as gr

ggsearch = GoogleSearch()

def QA(text):
    _, documents = ggsearch.search(text)
    passages = rel_ranking(text, documents)
    top_passage = passages[0]["text"] if len(passages) > 0 else "No answer found."
    return top_passage

input_text = gr.inputs.Textbox(label="Nhập câu hỏi:")
output_text = gr.outputs.Textbox(label="Câu trả lời:")

gr.Interface(fn=QA, inputs=input_text, outputs=output_text).launch()