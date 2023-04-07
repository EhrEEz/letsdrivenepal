from django.contrib.auth.base_user import BaseUserManager


class AccountManager(BaseUserManager):

    use_in_migrations = True

    def create_user(
        self, phone_number, first_name, last_name, role, dob, password=None
    ):
        if not phone_number:
            return ValueError("Phone Number is required")

        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            role=role,
            dob=dob,
        )
        user.set_password(password)
        user.is_superuser = False
        user.is_active = True
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        phone_number,
        first_name,
        last_name,
        role,
        dob,
        password=None,
        **extrafields
    ):
        if not password:
            ValueError("Do Not Leave The Password Blank")
        if role == 0:
            user = self.create_user(
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                role=role,
                dob=dob,
                password=password,
                **extrafields
            )
            user.is_superuser = True
            user.is_staff = True
            user.save(using=self._db)
            return user
        else:
            return ValueError("You are not eligible to become a superuser")