from rest_framework import serializers
from .models import Book
# from .validators import title_and_author_not_identical_validator

def one_to_five(value):
    if not 0 <= value <= 5:
        raise serializers.ValidationError("Рейтинг должен быть от 0 до 5")


class One_To_Five:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
    
    def __call__(self, value):
        if not self.min_value <= value <= self.max_value:
            raise serializers.ValidationError("Рейтинг должен быть от 0 до 5")


# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200, default="Django REST Framework")
#     author = serializers.CharField(max_length=100)
#     ratings = serializers.IntegerField(validators=[one_to_five])

#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.author = validated_data.get("author", instance.author)
#         instance.save()
#         return instance

#     def validate_title(self, value):
#         if "django" not in value.lower():
#             raise serializers.ValidationError("В имени должно присутствовать слово django!")
#         return value
    
#     def validate(self, data):
#         if data["title"].lower() == data["author"].lower():
#             raise serializers.ValidationError("Введены одинаковые значения полей")
#         return data

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        extra_kwargs = {
            "ratings": {"required": False}
        }
    
    def validate_title(self, value):
        if "django" not in value.lower():
            raise serializers.ValidationError("В имени должно присутствовать слово django!")
        return value
    
    # validators = [
    #     title_and_author_not_identical_validator,
    # ]