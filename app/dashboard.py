from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard
from jet.dashboard.models import UserDashboardModule


class CustomIndexDashboard(Dashboard):
    columns = 3

    def get_or_create_module_models(self, user):
        module_models = []

        i = 0

        for module in self.children:
            column = module.column if module.column is not None else i % self.columns
            order = module.order if module.order is not None else int(i / self.columns)

            obj, created = UserDashboardModule.objects.get_or_create(
                title=module.title,
                app_label=self.app_label,
                user=user.pk,
                module=module.fullname(),
                column=column,
                order=order,
                settings=module.dump_settings(),
                children=module.dump_children(),
            )
            module_models.append(obj)
            i += 1

        return module_models

    # Loads the dashboard on reload
    def load_modules(self):
        module_models = self.get_or_create_module_models(self.context["request"].user)

        loaded_modules = []

        for module_model in module_models:
            module_cls = module_model.load_module()
            if module_cls is not None:
                module = module_cls(model=module_model, context=self.context)
                loaded_modules.append(module)

        self.modules = loaded_modules

    def init_with_context(self, context):
        self.children.append(
            modules.ModelList(
                _(
                    "User Management",
                ),
                models=(
                    "auth.User",
                    "user_profile.UserProfile"
                ),
                column=2,
                order=2,
            )
        )
        self.children.append(
            modules.ModelList(
                _(
                    "Authentication & Authorization",
                ),
                models=("authtoken.TokenProxy", "auth.Group"),
                column=0,
                order=1,
            )
        )
        self.children.append(
            modules.ModelList(
                _(
                    "Blog Content",
                ),
                models=("blog.Blog", "user_profile.Tag", "user_profile.Interest"),
                column=0,
                order=2,
            )
        )
