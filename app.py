import os
from flask import Flask, render_template, request, send_file
from moviepy.editor import VideoFileClip

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def extract_audio(video_path, audio_output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_output_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_audio', methods=['POST'])
def extract_audio_route():
    video_file = request.files['video']
    if video_file and video_file.filename.endswith(('.mp4', '.avi', '.mov', '.wmv')):
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], 'input_video.mp4')
        audio_output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output_audio.mp3')
        video_file.save(video_path)
        extract_audio(video_path, audio_output_path)
        return send_file(audio_output_path, as_attachment=True)
    else:
        return "El archivo no es un video válido. Por favor, seleccione un archivo de video."

if __name__ == '__main__':
    app.run(debug=True)
