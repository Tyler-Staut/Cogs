import requests

def upload_url_to_hybrid_analysis(url, api_key):
    """
    Uploads a URL to Hybrid Analysis and returns the URL to view the results.
    """
    url = "https://www.hybrid-analysis.com/api/v2/submit/url"
    headers = {"api-key": api_key}
    data = {"url": url}
    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()
    sha256 = response_json["sha256"]
    return f"https://www.hybrid-analysis.com/sample/{sha256}"

def upload_file_to_hybrid_analysis(file_path, api_key):
    """
    Uploads a file to Hybrid Analysis and returns the URL to view the results.
    """
    url = "https://www.hybrid-analysis.com/api/v2/submit/file"
    headers = {"api-key": api_key}
    files = {"file": open(file_path, "rb")}
    response = requests.post(url, headers=headers, files=files)
    response_json = response.json()
    sha256 = response_json["sha256"]
    return f"https://www.hybrid-analysis.com/sample/{sha256}"
