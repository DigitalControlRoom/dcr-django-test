from django.http import JsonResponse


def stats(request):
    # TODO - Provide name, number_countries and total_population for each region
    response = {"regions": []}

    return JsonResponse(response)
