// var url = "http://www.newyorker.com/magazine/2015/02/23/pain-gain";
var url;

$('#submit').on('click', function() {
	url = $('#article-link').val();
});

$.getJSON("http://socialite-api.herokuapp.com/tweets?url=" + url, function(data) {
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
		// $('body').append('<p>' + tweets[i].tweet + '</p>');
		// $('body').append('<p>' + tweets[i].retweet_count + '</p>');
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

		// tweets with both single and double quotation marks, but no article title or keywords
		// search all tweet text
		// if tweet contains article title OR keywords in both single AND double quotation marks, DO NOT add to array
		// else push to tweets_to_search array
		// what about quotes within quotes??
		// ((element.indexOf(double_quotes) > -1) && (element.indexOf(single_quotes) > -1))
		// tweets that DO NOT contain single quotes and article title are pushed into array
		

		// tweets that DO NOT contain double quotes and first keyword are pushed into array
		

		for (var j = 0; j < keywords.length; j++) {
			if (tweet_text.indexOf(double_quotes + keywords[j]) > -1) {
				// console.log("double quotes WITH keyword");
				num_tweets_with_keywords++;
			} else if (tweet_text.indexOf(single_quotes + keywords[j]) > -1) {
				// console.log("single quotes WITH keyword");
				num_tweets_with_keywords++;
			}
		}
	}

	// var tweets_to_search = [];
	var tweets_enclosed_quotations = all_tweets_text.filter(containsQuotedText).filter(noArticleTitle);

	/*
		1) Get tweets that are encased in 'single' or "double" quotes /
		2) Filter out all tweets that ONLY contain the article title or keywords in single/double quotations and nothing else
		3) Figure out some way to get the tweets that have nested quotation marks
		4) Remove duplicates!!
	*/

	// check if tweets have text enclosed in single or double quotes
	function containsQuotedText(element) {
		var current_tweet = element.toLowerCase();
		return ((current_tweet.match(/"(.*?)"/)) || (current_tweet.match(/'(.*?)'/)));
	}

	function containsKeywordOnly(element) {
		var current_tweet = element.toLowerCase();
		// get tweets that contain the article title in quotes, but also have other quotation marks?
		return ((!(current_tweet.match(double_quotes + keywords[2]))) && (!(current_tweet.match(double_quotes + article_title))) && (!(current_tweet.match(single_quotes + article_title))));
	}

	// checks if tweets have article title in single or double quotes (most tweets that do don't have quotes)
	function noArticleTitle(element) {
		var current_tweet = element.toLowerCase();
		return ((!(current_tweet.match(double_quotes + article_title))) && (!(current_tweet.match(single_quotes + article_title))));
	}

	console.log(tweets_enclosed_quotations.length);
	for (var q = 0; q < tweets_enclosed_quotations.length; q++) {
		$('body').append('<p>' + tweets_enclosed_quotations[q] + '</p>');
	}

	// for (var t=0; t < all_tweets_text.length; t++) {
	// 	var current_tweet = all_tweets_text[t].toLowerCase();
	// 	// only search tweets with quotation marks
	// 	if ((current_tweet.indexOf(double_quotes) == -1) && (current_tweet.indexOf(single_quotes) == -1)) {
	// 		// // tweets that DO NOT contain double quotes and article title, or article title are pushed into array
	// 		if ((current_tweet.indexOf(double_quotes + article_title) == -1) && (current_tweet.indexOf(single_quotes + article_title) == -1) && (current_tweet.indexOf(article_title) == -1)) {
	// 			var text_to_push = {};
	// 			text_to_push["text"] = current_tweet;
	// 			tweets_to_search.push(text_to_push);	
	// 		}
	// 	}
	// }

	console.log('total number of scraped tweets ' + tweets.length);
	console.log('tweets with favorites ' + num_favs);
	console.log('tweets with retweets ' + num_retweets);
	console.log('tweets with hashtags ' + num_hashtags);
	console.log('tweets with user mentions ' + num_mentions);
	console.log('tweets with author mentions ' + num_author);
	console.log('tweets with publication mentions ' + num_pub_mentions);
	console.log('tweets with publication name ' + num_pub);
	console.log('tweets with article title ' + num_title);
	console.log('tweets that have RTs ' + num_rt);
	// console.log('number of duplicate tweets ' + tweetFreq(all_tweets_text));
	console.log('number of unique tweets with duplicates ' + sameTweets(tweetFreq(all_tweets_text)));
	console.log('number of duplicate tweets ' + duplicateTweets(tweetFreq(all_tweets_text)));

	$('body').append('<p><b>total number of scraped tweets</b> ' + tweets.length + "</p>");
	$('body').append('<p><b>tweets with favorites</b> ' + num_favs + "</p>");
	$('body').append('<p><b>tweets with retweets</b> ' + num_retweets + "</p>");
	$('body').append('<p><b>tweets with hashtags</b> ' + num_hashtags + "</p>");
	$('body').append('<p><b>tweets with user mentions</b> ' + num_mentions + "</p>");
	$('body').append('<p><b>tweets with author mentions</b> ' + num_author + "</p>");
	$('body').append('<p><b>tweets with publication mentions</b> ' + num_pub_mentions + "</p>");
	$('body').append('<p><b>tweets with publication name</b> ' + num_pub + "</p>");
	$('body').append('<p><b>tweets with article title</b> ' + num_title + "</p>");
	$('body').append('<p><b>tweets that have RTs</b> ' + num_rt + "</p>");
	// console.log('number of duplicate tweets ' + tweetFreq(all_tweets_text));
	$('#tweet-data').append('<p><b>number of unique tweets with duplicates</b> ' + sameTweets(tweetFreq(all_tweets_text)) + "</p>");
	$('#tweet-data').append('<p><b>number of duplicate tweets</b> ' + duplicateTweets(tweetFreq(all_tweets_text)) + "</p>");
	$('#tweet-data').append('<p><b>number of tweets with double quotation marks</b> ' + num_double_quotes + "</p>");
	$('#tweet-data').append('<p><b>number of tweets with single quotation marks</b> ' + num_single_quotes + "</p>");
	$('#tweet-data').append('<p><b>number of tweets with quotation marks with headline</b> ' + num_quotes_with_title + "</p>");
	$('#tweet-data').append('<p><b>number of tweets with quotation marks without headline</b> ' + (num_double_quotes + num_single_quotes - num_quotes_with_title) + "</p>");
	$('#tweet-data').append('<p><b>number of tweets with quotation marks with keywords</b> ' + (num_tweets_with_keywords) + "</p>");
	$('#tweet-data').append('<p><b>number of tweets with quotation marks without headline or keywords</b> ' + (num_double_quotes + num_single_quotes - num_quotes_with_title - num_tweets_with_keywords) + "</p>");
	// console.log(tweets_to_search);
	// for (var k = 0; k < tweets_to_search.length; k++) {
	// 	$('body').append('<p>' + tweets_to_search[k].text + '</p>');
	// }
	//printAllTweets(tweetFreq(all_tweets_text));
	for (var qt = 0; qt < tweets_enclosed_quotations.length; qt++) {
		console.log(tweets_enclosed_quotations[qt]);
		var tweet_quote = tweets_enclosed_quotations[qt].match(/"(.*?)"/);
		if (tweet_quote !== null) {
			af.log(tweet_quote[qt]);
			$('#output p').highlight(tweet_quote[qt]); //needed to be a variable because [1] was showing the second tweet repeatedly
		}
	}
	// $('.container p').highlight("How much of a sex film can this be, given that the people most likely to be turned on by it are lawyers?");
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
			// console.log(j + ": " + input[j]);
			same_tweets++;
		}
	}
	return same_tweets;
}

function duplicateTweets(input) {
	var duplicate_tweets = 0;

	for (var j in input) {
		if (input[j] > 1) {
			// console.log(j + ": " + input[j]);
			duplicate_tweets = duplicate_tweets + input[j] - 1;
		}
	}
	return duplicate_tweets;
}

$(document).ready(function() {
	// $('p:contains("How much of a sex film can this be, given that the people most likely to be turned on by it are lawyers?")').addClass('selected');
	
});