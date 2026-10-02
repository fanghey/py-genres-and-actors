import init_django_orm  # noqa: F401

from db.models import Actor, Genre


def main():
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Drama")

    Actor.objects.create(
        first_name="George",
        last_name="Clooney",
    )
    Actor.objects.create(
        first_name="Keanu",
        last_name="Reeves",
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Keegan",
    )
    Actor.objects.create(
        first_name="Will",
        last_name="Smith",
    )
    Actor.objects.create(
        first_name="Jaden",
        last_name="Smith",
    )
    Actor.objects.create(
        first_name="Scarlett",
        last_name="Johansson",
    )

    drama = Genre.objects.get(name="Drama")
    drama.name = "Drama"
    drama.save()

    george = Actor.objects.get(first_name="George")
    george.last_name = "Clooney"
    george.save()

    keanu = Actor.objects.get(last_name="Reeves")
    keanu.first_name = "Keanu"
    keanu.last_name = "Reeves"
    keanu.save()

    Genre.objects.get(name="Action").delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
