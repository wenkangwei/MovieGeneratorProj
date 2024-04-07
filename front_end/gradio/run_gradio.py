import gradio as gr
import fire
class GradioApp:
    def __init__(self, model=None):
        self.model = model
        if self.model is None:
            self.model_func = lambda x: f"Hi man, I got your text: {x}"
        else:
            self.model_func = self.model.query

    def run(self):
        gr.Interface(
            fn=self.model_func,
            inputs='textbox',
            outputs="textbox",
            title="Movie Generator",
            description="Generate a movie plot based on the input text.",
            theme="huggingface",
            examples=[
                ["A group of friends go on a road trip to find a hidden treasure."],
                ["A scientist discovers a way to travel through time."],
                ["A group of survivors try to escape a zombie apocalypse."],
            ],
        ).launch(share=True)

if __name__ == "__main__":
    GradioApp().run()