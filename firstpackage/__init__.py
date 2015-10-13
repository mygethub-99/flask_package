from flask import Flask, render_template, session, g 


app = Flask(__name__)

import firstpackage.database

import firstpackage.menu_view
