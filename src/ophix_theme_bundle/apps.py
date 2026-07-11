from django.apps import AppConfig


class OphixThemeBundleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ophix_theme_bundle"
    verbose_name = "Theme: Bundle"

    def ready(self):
        from django.db.models.signals import post_migrate
        from django.apps import apps
        # Fire after admin_interface migrations — guarantees the Theme
        # table exists. The receiver is idempotent: skips themes that are
        # already installed. install_bundled_theme() iterates every
        # subdirectory under themes/, so all bundled themes install in
        # one pass.
        post_migrate.connect(
            _install_on_migrate,
            sender=apps.get_app_config("admin_interface"),
        )


def _install_on_migrate(sender, **kwargs):
    from admin_interface.utils import install_bundled_theme
    from django.apps import apps
    install_bundled_theme(apps.get_app_config("ophix_theme_bundle"))
