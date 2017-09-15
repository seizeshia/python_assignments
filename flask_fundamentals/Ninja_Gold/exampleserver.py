from flask import Flask, render_template, request, redirect, session
import random, datetime

app= Flask(__name__)
app.secret_key = "IsThisEasyMode"
