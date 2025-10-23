from flask import Flask, render_template

# إنشاء التطبيق
app = Flask(__name__)

# الراوت الرئيسي
@app.route("/")
def main():
    model = {"title": "Hello Build Trigger."}
    return render_template("index.html", model=model)

# تشغيل التطبيق لو الملف اتشغّل مباشرة
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
