from flask import Flask, jsonify, request
import csv
 
all_articles = []
 
with open('articles.csv', encoding="utf-8") as f:
    reader = csv.reader(f) 
    data = list(reader) 
    all_articles = data[1:] 
 
liked_articles = []
disliked_articles = []