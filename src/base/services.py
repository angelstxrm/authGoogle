from django.core.exceptions import ValidationError

# Не понимаб для чего это нужно, если можно передать путь в upload_to, но пусть будет)
def get_path_upload_avatar(instance, file):
    '''
    Построение пути к файлу аватара пользователя. Format: (media/avatar/user_id/avatar.jpg)
    '''
    return f'avatar/{instance.id}/{file}'

def validate_size_image(file_obj):
    '''
    Проверка размера изображения
    '''
    megabite_limit = 2
    if file.obj.size > megabite_limit * 1024 * 1024:
        raise ValidationError(f'Размер файла не должен превышать {megabite_limit} мегабайт')