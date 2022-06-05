{
	'feed': {
		'@xmlns:yt': 'http://www.youtube.com/xml/schemas/2015',
		'@xmlns': 'http://www.w3.org/2005/Atom',
		'link': [
			{'@rel': 'hub', '@href': 'https://pubsubhubbub.appspot.com'},
			{'@rel': 'self', '@href': 'https://www.youtube.com/xml/feeds/videos.xml?channel_id=UCA-ZGJRoU4gVNEhuIYWKFBg'}
		],
		'title': 'YouTube video feed',
		'updated': '2022-06-03T16:35:42.431084384+00:00',
		'entry': {
			'id': 'yt:video:d2tVoKx9918',
			'yt:videoId': 'd2tVoKx9918',
			'yt:channelId': 'UCA-ZGJRoU4gVNEhuIYWKFBg',
			'title': 'Code test',
			'link': {
				'@rel': 'alternate',
				'@href': 'https://www.youtube.com/watch?v=d2tVoKx9918'
			},
			'author': {
				'name': 'Coding with Liz',
				'uri': 'https://www.youtube.com/channel/UCA-ZGJRoU4gVNEhuIYWKFBg'
			},
			'published': '2022-06-03T16:29:22+00:00',
			'updated': '2022-06-03T16:35:42.431084384+00:00'
		}
	}
}


# on delete
{
	'feed': {
		'@xmlns:at': 'http://purl.org/atompub/tombstones/1.0',
		'@xmlns': 'http://www.w3.org/2005/Atom',
		'at:deleted-entry': {
			'@ref': 'yt:video:WfHApINjvBY',
			'@when': '2022-06-04T14:24:46.723265+00:00',
			'link': {'@href': 'https://www.youtube.com/watch?v=WfHApINjvBY'},
			'at:by': {
				'name': 'Coding with Liz',
				'uri': 'https://www.youtube.com/channel/UCA-ZGJRoU4gVNEhuIYWKFBg'
			}
		}
	}
}

#name change
{
	'feed': {
		'@xmlns:yt': 'http://www.youtube.com/xml/schemas/2015',
		'@xmlns': 'http://www.w3.org/2005/Atom',
		'link': [{'@rel': 'hub', '@href': 'https://pubsubhubbub.appspot.com'}, {'@rel': 'self', '@href': 'https://www.youtube.com/xml/feeds/videos.xml?channel_id=UCA-ZGJRoU4gVNEhuIYWKFBg'}],
		'title': 'YouTube video feed',
		'updated': '2022-06-05T09:55:21.30273681+00:00',
		'entry': {
			'id': 'yt:video:Fp2dHNYEs40',
			'yt:videoId': 'Fp2dHNYEs40',
			'yt:channelId': 'UCA-ZGJRoU4gVNEhuIYWKFBg',
			'title': 'catch name change api changed name',
			'link': {'@rel': 'alternate', '@href': 'https://www.youtube.com/watch?v=Fp2dHNYEs40'},
			'author': {'name': 'Coding with Liz', 'uri': 'https://www.youtube.com/channel/UCA-ZGJRoU4gVNEhuIYWKFBg'},
			'published': '2022-06-05T09:53:06+00:00',
			'updated': '2022-06-05T09:55:21.30273681+00:00'
		}
	}
}