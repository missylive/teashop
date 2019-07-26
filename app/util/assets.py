from flask_assets import Bundle, Environment
from .. import app

bundles = {

        'ts_js': Bundle(
            'bootstrap/js/bootstrap.min.js',
            output='gen/ts.js'),

        'ts_css': Bundle(
            'bootstrap/css/bootstrap.min.css',
            'fonts/font-awesome.min.css',
            'fonts/ionicons.min.css',
            'css/Footer-Basic.css',
            'css/Lightbox-Gallery.css',
            'css/Login-Form-Clean.css',
            'css/Navigation-Clean.css',
            'css/styles.css',
            output='gen/ts.css')
}

assets = Environment(app)

assets.register(bundles)


