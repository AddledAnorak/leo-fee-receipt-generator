from flask import Flask, request, render_template
import edit
import random

app = Flask(
	__name__,
	template_folder='templates',
	static_folder=''
)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/create', methods=['POST'])
def create():
	data = dict(request.form)

	with open('id.txt', 'r') as f:
		receipt_id = f.read().strip('\n')

	with open('id.txt', 'w') as f:
		f.write(str(int(receipt_id) + 1))

	while len(receipt_id) < 3:
		receipt_id = '0' + receipt_id

	data['receipt-id'] = receipt_id
	img_path = edit.run(data, save=True, show=False)

	return render_template('create.html', download_path=img_path)



if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = random.randint(1000, 8000))
