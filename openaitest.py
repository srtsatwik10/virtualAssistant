import os
import openai


openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="prompt",
  temperature=1,
  max_tokens=500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)



'''{
  "id": "cmpl-7SS6NgGX5G9kPziQ8EWlixAGpGSiX",
  "object": "text_completion",
  "created": 1687015563,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "The Foreign Secretary and the Ministers for Africa, Dominic Raab and James Duddridge met the Foreign Minister of Ethiopia, Dr Gedu Andarge on Thursday 9th July.\n\nThe Foreign Secretary thanked Ethiopia for playing an important and constructive role in the region, particularly in helping the Government of South Sudan move towards the formation of a transitional government and its support for the ongoing peace process in Sudan. He and Ministers Duddridge and Raab agreed with the Ethiopian Foreign Minister that democratic reform and the development of governance and human rights are essential if the region is to realise its potential.\n\nThe Foreign Secretary discussed with the Foreign Minister the importance of strong bilateral ties between the UK and Ethiopia and agreed to strengthen collaboration in areas such as security, trade and prosperity, democracy and human rights, and economic reforms.\n\nThe Foreign Secretary and Ministers welcomed recent developments in Ethiopia, such as the release of political prisoners and the approval of the Multilingual Education Proclamation. It was agreed that the UK and Ethiopia should continue to work together on issues related to democracy, human rights and economic reforms.\n\nThe Foreign Secretary also welcomed the launch of Ethiopia\u2019s third International Democracy and Human Rights Symposium in Addis Ababa, and the recent enactment of a new Charities and Societies Proclamation, which allows for the legal registration of organisations, including political parties, carrying out activities in the public interest.\n\nThe Foreign Secretary welcomed the Human Rights Council scrutiny of the post-conflict situation in Ethiopia and the UN Human Rights Office\u2019s visit to Ethiopia in May. He encouraged the Government of Ethiopia to continue its engagement with the Human Rights Council and to work with the UN Human Rights Office to protect human rights in Ethiopia.\n\nThe Foreign Secretary and Ministers discussed the importance of Ethiopia\u2019s continued commitment to regional peace and security and to its efforts in promoting reconciliation and dialogue in the region. They encouraged Ethiopia\u2019s cooperation with regional organisations, such as the African Union and IGAD, and renewed their call on all stakeholders to ensure a peaceful and enduring solution to the conflict in Tigray.\n\nThe Foreign Secretary and Ministers also raised the importance of Ethiopia hosting refugees on its territory, including Somalis who are fleeing conflict and persecution in Somalia. The UK will continue to support Ethiopia\u2019s efforts to ensure the safety and protection of refugees, including through the Ethiopia Joint Response Plan. They also discussed Ethiopia\u2019s efforts to protect its environment and agreed to explore future",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 1,
    "completion_tokens": 500,
    "total_tokens": 501
  }
}'''