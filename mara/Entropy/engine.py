
import json
from pathlib import Path
from data import Data
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header , Digits, Input, Label, Button
from textual.widget import Widget
from textual.containers import Center,Horizontal,VerticalScroll
from textual.reactive import reactive
import json
from file_logic import display, burn 

class Displayer(Horizontal):

    CSS_PATH = "test.tcss"
    

    def compose(self) -> ComposeResult:
        yield Name()
        self.inputs = Input(placeholder="Enter spending amount",id="input",type="integer")
        yield self.inputs
        yield Button("Submit", id="burn")
    def on_pressed(self): 
        test = burn("D:\mara\Entropy\entropy.json",self.inputs.value)
        
class Name(Widget): 
    who = reactive("name")
    def render(self) -> str:
        return f"{self.who}"




class Entropy(App):
    """
    Docstring for Entropy: 
    Entropy is a simple system,
    weekly total. 
    daily total
    daily input

    """ 
    BINDINGS = [("d","toogle_dark","Toggle dark mode")]
    CSS_PATH = "test.tcss"
    who = reactive("name")
    def render(self) -> str:
        return f"{self.who}"
    def compose(self) -> ComposeResult:
        data = display("D:\mara\Entropy\entropy.json")
        yield Header()
        yield VerticalScroll(Displayer())
        yield Footer()
    def on_input_submitted(self, event: Input.Submitted) -> None:
        pass

    def action_toggle_dakr(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    def on_mount(self):
        pass

if __name__ == "__main__":
    app = Entropy()
    app.run()


        
