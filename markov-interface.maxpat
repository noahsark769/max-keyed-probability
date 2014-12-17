{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 6,
			"minor" : 1,
			"revision" : 8,
			"architecture" : "x86"
		}
,
		"rect" : [ 4.0, 44.0, 978.0, 710.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 0,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 0,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"boxanimatetime" : 200,
		"imprint" : 0,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"boxes" : [ 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"frgb" : 0.0,
					"id" : "obj-9",
					"linecount" : 3,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 1070.0, 17.0, 290.0, 47.0 ],
					"text" : "Inlet 4: Bang to reset\n\nNot implemented yet."
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"frgb" : 0.0,
					"id" : "obj-8",
					"linecount" : 17,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 714.0, 17.0, 290.0, 234.0 ],
					"text" : "Inlet 3: Bang to query data\n\nWhen this inlet is banged, data will be queried from the KeyedMarkovEmitter and returned as an odot packet with the following form:\n\n[\n    [\n        [[\"snare\": 0],\n        [\"kick\": 1],\n        ...\n    ],\n    ...\n]\n\nWhere the 1 specifies that the key should be played this interval, and the 0 specifies that it shouldn't."
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"frgb" : 0.0,
					"id" : "obj-7",
					"linecount" : 8,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 384.0, 17.0, 277.0, 114.0 ],
					"text" : "Inlet 2: Bang to train\n\nWhen banged, this inlet collected all the training data that its seen so far, serializes it, then sends it to the MarkovEmitter (in the python OSC server) via UDP. After this, the probalistic generator will know about the training data, and you can expect it to output correct data when Inlet 3 is banged."
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 12.0,
					"frgb" : 0.0,
					"id" : "obj-6",
					"linecount" : 16,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 60.0, 17.0, 276.0, 221.0 ],
					"text" : "Inlet 1: Accepts training data.\n\nThis inlet accepts an odot packet with the following keys:\n\n\\key: the key to train the data on, like \"snare\" or \"kick\"\n\\offset: the millisecond offset from the start of the training sequence when the specified key was detected.\n\nThis patcher collects this training data until inlet 2 is banged, at which point it communicates the compiled training data to the python implementation of KeyedMarkovEmitter via UDP/OSC."
				}

			}
, 			{
				"box" : 				{
					"comment" : "Bang to reset",
					"id" : "obj-4",
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1024.0, 17.0, 25.0, 25.0 ]
				}

			}
, 			{
				"box" : 				{
					"comment" : "Bang to output saved data",
					"id" : "obj-3",
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 679.0, 17.0, 25.0, 25.0 ]
				}

			}
, 			{
				"box" : 				{
					"comment" : "Bang to \"train\" on a sequence",
					"id" : "obj-2",
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 345.0, 17.0, 25.0, 25.0 ]
				}

			}
, 			{
				"box" : 				{
					"comment" : "Accepts training data",
					"id" : "obj-1",
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 28.0, 17.0, 25.0, 25.0 ]
				}

			}
 ],
		"lines" : [  ],
		"dependency_cache" : [  ]
	}

}
