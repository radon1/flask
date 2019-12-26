from flask import Flask, request, render_template, redirect
from flask_admin import Admin
from flask_admin.model import BaseModelView
from flask_mongoengine import MongoEngine
from werkzeug.utils import secure_filename
from api import api_bp
from forms import UserForm
from models import UserV
import os
from flask.views import MethodView


db = MongoEngine()

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_db',
    'host': 'localhost',
    'port': 27017
}
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='web_app', template_mode='bootstrap3')
app.register_blueprint(api_bp)


class MyModelView(BaseModelView):
    def scaffold_list_columns(self):
        return ['first_name', 'last_name']

    def scaffold_sortable_columns(self):
        return {}

    def scaffold_form(self):
        return UserForm

    def get_list(self, page, sort_field, sort_desc, search, filters,
                 page_size=None):
        for flt, value in filters:
            query = self._filters[flt].apply(query, value)


admin.add_view(MyModelView(UserV))

db.init_app(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


class AddPost(MethodView):
    def post(self):
        form = UserForm(request.form)
        target = os.path.join(APP_ROOT, 'static\images')
        if form.validate():
            filename = secure_filename(request.files["image4"].filename)
            destination = "\\".join([target, filename])
            request.files['image4'].save(destination)
            user = UserV()
            form.populate_obj(user)
            user.image3 = f"images/{request.files['image4'].filename}"
            user.save()
            return redirect('/')

    def get(self):
        form = UserForm()
        page = 1
        if request.args.get("page"):
            page = int(request.args.get("page"))
        paginate_users = UserV.objects.paginate(page=page, per_page=3)
        return render_template('hello.html', form=form, paginated_users=paginate_users)


app.add_url_rule('/', view_func=AddPost.as_view('add_post'))


if __name__ == '__main__':
    app.run()
