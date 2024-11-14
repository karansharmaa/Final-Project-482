from flask import Flask, request, jsonify
#from your_nlp_module import get_review_summary, get_review_rating  # assuming you have a function to handle processing

app = Flask(__name__)

@app.route('/api/review', methods=['POST'])
def review():
    data = request.get_json()
    media_type = data.get('mediaType')
    media_name = data.get('mediaName')

    # NLP processing to get rating and summary
    rating = get_review_rating(media_type, media_name)
    summary = get_review_summary(media_type, media_name)

    return jsonify({"rating": rating, "summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
