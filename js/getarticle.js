// var userURL = "https://medium.com/message/how-paper-magazines-web-engineers-scaled-kim-kardashians-back-end-sfw-6367f8d37688";
// var userURL = "http://www.newyorker.com/magazine/2015/02/23/pain-gain";
// https://medium.com/message/yes-to-the-dress-5ec06c06aca4


$(document).ready(function() {
	var userURL;
	var file;
	//validate url from user

	$('#50shades').on('click', function() {
		userURL = 'http://www.newyorker.com/magazine/2015/02/23/pain-gain';
		$('#article-link').val(userURL);
		file = 'articles/50shades.json';
	});

	$('#dress').on('click', function() {
		userURL = 'https://medium.com/message/yes-to-the-dress-5ec06c06aca4';
		$('#article-link').val(userURL);
		file = 'articles/dress.json';
	});

	$('#submit').on('click', function() {
		// clear existing data out
		$('#output').empty();
		$('#tweet-data').empty();
		//need to figure out how to submit form on enter
		userURL = $('#article-link').val();
		console.log(userURL);
		// jQuery method chains
		userURL = userURL.replace(/:/g , "%3A").replace(/\//g, "%2F");

		// concatenating a URL
		// using ajax to call the embedly API and add my key and other stuff to each URL
		$.ajax({
	  		url: "http://api.embed.ly/1/extract?key=f2f84ff5013b443ab711b204590d9aa2&url=" + userURL + "&maxwidth=500",
	  		context: document.body
		}).done(function(data) {
		  	// console.log(data["content"]);
		  	// we only want this to happen when the user puts the link of the article in the form OBVIOUSLAY
		  	console.log("it's working!")
		  	$('#output').append('<p class="section-title">Article</p>' + data["content"]);
		  	getFile();
		});
		
		// janky solution idk???
		function getFile() {
			// $.getJSON("http://socialite-api.herokuapp.com/tweets?url=" + userURL, function(data) {
			$.getJSON(file, function(data) {
				window.data = data;
				var tweets = [],
					all_tweets_text = [],
					num_favs = 0,
					num_retweets = 0,
					num_rt = 0;
					num_hashtags = 0,
					num_mentions = 0,
					num_author = 0,
					num_pub_mentions = 0,
					num_pub = 0,
					num_title = 0,
					num_double_quotes = 0,
					num_single_quotes = 0,
					num_quotes_with_title = 0,
					num_keywords = 0,
					num_tweets_with_keywords = 0;

				$.each(data, function(key, val) {
					tweets.push(val);
				});

				// console.log(tweets);
				var author_handle = "";
				var pub_handle = "@newyorker";
				var pub_name = "the new yorker";
				var article_title = 'no pain, no gain';
				var keywords = ["50 shades of grey", "fifty shades of grey", "50 shades"];
				var double_quotes = '"';
				var single_quotes = "'"; // also includes apostrophes!
				
				for (var i=0; i < tweets.length; i++) {
					if (tweets[i].favorited == true)
						num_favs++;
					if (tweets[i].retweet_count > 0)
						num_retweets++;
					if (tweets[i].hashtags.length > 0)
						num_hashtags++;
					if (tweets[i].user_mentions.length > 0)
						num_mentions++;

					var tweet_text = tweets[i].tweet;
					all_tweets_text.push(tweet_text);

					var tweet_text = tweets[i].tweet.toLowerCase();

					if (tweet_text.indexOf(author_handle) > -1)
						num_author++;
					if (tweet_text.indexOf(pub_handle) > -1)
						num_pub_mentions++;
					if (tweet_text.indexOf(pub_name) > -1)
						num_pub++;
					if (tweet_text.indexOf(article_title) > -1)
						num_title++;
					if (tweet_text.indexOf("rt") > -1)
						num_rt++;
					if (tweet_text.indexOf(double_quotes) > -1)
						num_double_quotes++;
					if (tweet_text.indexOf(single_quotes) > -1)
						num_single_quotes++;
					if (tweet_text.indexOf(double_quotes + article_title) > -1) {
						num_quotes_with_title++;
					}
					if (tweet_text.indexOf(single_quotes + article_title) > -1) {
						num_quotes_with_title++;
					}

					for (var j = 0; j < keywords.length; j++) {
						if (tweet_text.indexOf(double_quotes + keywords[j]) > -1) {
							num_tweets_with_keywords++;
						} else if (tweet_text.indexOf(single_quotes + keywords[j]) > -1) {
							num_tweets_with_keywords++;
						}
					}
				}

				var tweets_enclosed_quotations = all_tweets_text.filter(containsQuotedText).filter(noArticleTitle);

				// check if tweets have text enclosed in single or double quotes
				function containsQuotedText(element) {
					var current_tweet = element.toLowerCase();
					return ((current_tweet.match(/"(.*?)"/)) || (current_tweet.match(/'(.*?)'/)));
				}

				// checks if tweets have article title in single or double quotes (most tweets that do don't have quotes)
				function noArticleTitle(element) {
					var current_tweet = element.toLowerCase();
					return ((!(current_tweet.match(double_quotes + article_title))) && (!(current_tweet.match(single_quotes + article_title))));
				}

				$('#tweet-data').append('<p class="section-title">Tweet Data</p>');
				console.log(tweets_enclosed_quotations.length);
				for (var q = 0; q < tweets_enclosed_quotations.length; q++) {
					$('#tweet-data').append('<p>' + tweets_enclosed_quotations[q] + '</p>');
				}

				// $('#tweet-data').append('<p><b>number of unique tweets with duplicates</b> ' + sameTweets(tweetFreq(all_tweets_text)) + "</p>");
				// $('#tweet-data').append('<p><b>number of duplicate tweets</b> ' + duplicateTweets(tweetFreq(all_tweets_text)) + "</p>");
				// $('#tweet-data').append('<p><b>number of tweets with double quotation marks</b> ' + num_double_quotes + "</p>");
				// $('#tweet-data').append('<p><b>number of tweets with single quotation marks</b> ' + num_single_quotes + "</p>");
				// $('#tweet-data').append('<p><b>number of tweets with quotation marks with headline</b> ' + num_quotes_with_title + "</p>");
				// $('#tweet-data').append('<p><b>number of tweets with quotation marks without headline</b> ' + (num_double_quotes + num_single_quotes - num_quotes_with_title) + "</p>");
				// $('#tweet-data').append('<p><b>number of tweets with quotation marks with keywords</b> ' + (num_tweets_with_keywords) + "</p>");
				// $('#tweet-data').append('<p><b>number of tweets with quotation marks without headline or keywords</b> ' + (num_double_quotes + num_single_quotes - num_quotes_with_title - num_tweets_with_keywords) + "</p>");

				for (var qt = 0; qt < tweets_enclosed_quotations.length; qt++) {
					// console.log(tweets_enclosed_quotations[qt]);
					var tweet_quote = tweets_enclosed_quotations[qt].match(/"(.*?)"/);
					if (tweet_quote !== null) {
						var check_quote = tweet_quote[1].split(' ');
						console.log(tweet_quote[1]);
						if (check_quote.length > 4) {
							$('#output div').highlight(tweet_quote[1]);
						}
					}
				}
			});
		}
	});
});

function tweetText(tweet_text) {
	return tweet_text;
}

function tweetFreq(input) {
	var tweetArray = input;
	var returnArray = {};
	$.each(tweetArray, function(i, val) {
		if (returnArray[val]) {
			returnArray[val]++;
		} else {
			returnArray[val] = 1;
		}
	});
	return returnArray;
}

function printAllTweets(input) {
	var all_tweets = 0;

	for (var j in input) {
		console.log(j + ": " + input[j]);
		all_tweets++;
	}
}

function sameTweets(input) {
	var same_tweets = 0;

	for (var j in input) {
		if (input[j] > 1) {
			same_tweets++;
		}
	}
	return same_tweets;
}

function duplicateTweets(input) {
	var duplicate_tweets = 0;

	for (var j in input) {
		if (input[j] > 1) {
			duplicate_tweets = duplicate_tweets + input[j] - 1;
		}
	}
	return duplicate_tweets;
}