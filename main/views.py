from django.shortcuts import render
from googleapiclient.discovery import build
def home(request):
    return render(request, 'main/home.html')

def search_results(request):
    API_KEY = "AIzaSyBCRxP7cYY5D3oA8mb7aE-XdlTR4uKf-Jo"
    SEARCH_EGNINE_ID = "2f28fd59e50800b3a"
    search_results = []
    if request.method == "POST":
        query = request.POST['search_query']
        resource = build("customsearch", "v1", developerKey=API_KEY).cse()
        result = resource.list(q=query, cx=SEARCH_EGNINE_ID).execute()

        for item in result['items']:
            title = item['title']
            link = item['link']
            snippet = item['snippet']


            search_results.append((title, link, snippet))

        context = {
            "search_results": search_results,
        }
        return render(request, 'main/search_results.html', context)
    return render(request, 'main/search_results.html')
