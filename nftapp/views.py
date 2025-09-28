
from django.shortcuts import render

def home(request):
	"""Homepage for Kitsune Kodo NFT collection."""
	return render(request, "nftapp/home.html")
