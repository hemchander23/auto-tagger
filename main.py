from flashtext import KeywordProcessor
from flask import Flask, jsonify, render_template, request, Response
import keywords


api = Flask(__name__)

@api.route('/')
def hello_world():
   return render_template("index.html")


@api.route('/keywords', methods=['POST'])
def get_companies():
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_dict(keywords.keyword_dict)
    ip_data = request.get_json()
    print(ip_data)
    keywords_found = keyword_processor.extract_keywords(ip_data['post'], max_cost=1,span_info=True)
    print(keywords_found)
    return jsonify(keywords_found)
if __name__ == '__main__':
    api.run()
