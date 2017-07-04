kill $(ps aux | grep '[H]TTPBasicAuth_Server' | awk '{print $2}')
