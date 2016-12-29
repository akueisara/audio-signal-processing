import soundDownload as SD

Key = "UkShnu3foQ7noSWFbXZDOnQLic8S23hua0R7wqVX"

SD.downloadSoundsFreesound(queryText = 'bassoon', API_Key = Key, outputDir = 'tmp', topNResults = 20, duration = (0,5), tag = 'multisample')

SD.downloadSoundsFreesound(queryText = 'guitar', API_Key = Key, outputDir = 'tmp', topNResults = 20, duration = (0,3), tag = 'multisample')

SD.downloadSoundsFreesound(queryText = 'violin', API_Key = Key, outputDir = 'tmp', topNResults = 20, duration = (0,3), tag = 'multisample')
