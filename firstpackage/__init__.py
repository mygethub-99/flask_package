from flask import Flask, render_template, session


app = Flask(__name__)

import firstpackage.database

import firstpackage.menu_view
