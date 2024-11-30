from flask import Flask, render_template_string
import os

app = Flask(__name__)

# 画像フォルダのパス
IMAGE_FOLDER = r"C:\Users\fuya1\OneDrive\3.2.Creation 一般\3.ストック（アイデア・ネタ・サンプル） 一般\サンプル\3.作品毎\3.画集・同人・イラスト・グラフィック\2.イラスト T1\焦茶"  

# HTMLテンプレート
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Image Slideshow</title>
    <style>
        body { text-align: center; margin: 0; background: #000; color: white; }
        img { max-width: 100%; max-height: 90vh; display: block; margin: auto; }
    </style>
</head>
<body>
    {% for image in images %}
        <img src="{{ image }}" style="display:none;" class="slideshow">
    {% endfor %}
    <script>
        let slides = document.querySelectorAll('.slideshow');
        let index = 0;
        slides[index].style.display = 'block';

        setInterval(() => {
            slides[index].style.display = 'none';
            index = (index + 1) % slides.length;
            slides[index].style.display = 'block';
        }, 3000); // 3秒ごとに切り替え
    </script>
</body>
</html>
"""

@app.route('/')
def slideshow():
    # 画像ファイルを取得
    images = [f"/static/{img}" for img in os.listdir(IMAGE_FOLDER) if img.endswith(('jpg', 'png', 'gif'))]
    return render_template_string(HTML_TEMPLATE, images=images)

if __name__ == '__main__':
    # 静的ファイルをホスト
    app.static_folder = IMAGE_FOLDER
    app.run(debug=True)
