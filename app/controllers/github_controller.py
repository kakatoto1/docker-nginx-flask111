from flask import render_template
#don't change this import or it can't find the module controller
from  . controller import ControllerBase


class GithubController(ControllerBase):
    @staticmethod
    def get():
        name = "fan"
        return render_template('github.html', name=name)
