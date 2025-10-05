
from django.shortcuts import render

from .models import NFTRelease

def home(request):
	"""Homepage for Kitsune Kodo NFT collection."""
	releases = NFTRelease.objects.all().order_by('-launch_date', '-id')
	return render(request, "nftapp/home.html", {"releases": releases})
