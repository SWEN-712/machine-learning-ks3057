def random_color_func(word=None, font_size=None, position=None,
                      orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 21.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)


jenny = {'hearingadvocacy', 'USBLN16', 'WorldBrailleDay',
         'RepresentationMatters', 'Oscars2017', 'design', 'MSEnvision',
         'endals', 'MSInspire', 'WEDay',
         'AbilitySummit', 'microsofttranslator', 'NOWHITEFLAGS', 'NFB15',
         'Disabilityconfident',
         'KNFBReader', 'IDSL2018', 'MSFTGarage', 'CodeJumper', 'A11Y',
         'INForInclusion', 'DiversityandTech',
         'DriveforInclusion', 'OneNote', 'GDPR',
         'OfficeInsiders', 'DeafLeaders', 'FCC',
         'dyslexia', 'marmitethrone', 'BeFearless', 'CelebratingChampions',
         'usabilityTest', 'mEnabling19', 'DeafOutLoud',
         'AccessibilityAct', 'Rio2016', 'InsideXbox', 'Azure', 'WinML',
         'AIForAccessibility', 'career', 'inclusive_design', 'blind',
         'Deaf',
         'ChangetheWorld', 'inclusivetech', 'DiversityandInclusion',
         'Pride', 'AI', 'technology', 'MSBuild',
         'SmartCity', 'inclucity', 'disabilityemployment',
         'signlanguage', 'usbln15', 'MSEnvisionForum', 'Office365', 'asl',
         'XboxGC', 'EyeControl', 'StarbucksSigns', 'disabilities',
         'windowsCE', 'BEdeaffriendly',
         'Accessibility',
         'aapd', 'deaf', 'philanthropy', 'oscarsnerd', 'NAD',
         'LearningTogether', 'sketchnotes', 'XboxAdaptiveController',
         'g3ict',
         'GameChanger', 'call4brain', 'IDPD2016', 'DisabilityRights',
         'SeeingAI', 'Gears5', 'microsoftlife', 'cosp11',
         'AutismDay2016', 'UniteForParkinsons', 'inclusion', 'BREAKING',
         'MakeWhatsNext', 'SignLanguagesDay', 'Wired25', 'HackMars',
         'usbln17', 'chi2017', 'inclusivedesign', 'deaftalent',
         'AXSChat', 'STEM', 'AT_APPG',
         'Specialized', 'Inclusion', 'eyetrackingforwindows',
         'MicrosoftAbilitySummit', 'lalege',
         'Microsofts', 'autumncolors', 'colorblind', 'WEareOne', 'CAO',
         'britsabroad', 'LondonStrong', 'ChooseToInclude', 'Accessiblity',
         'assistivetech', 'designforall', 'Autism',
         'beforeandafter', 'WorldsMostEthicalCompanies', 'hurricaneharvey',
         'guidedogsawards', 'CRPD', 'AbilityHacks', 'Chester', 'vacation',
         'lovemyteam', 'CitiesUnlocked', 'ability2016', 'ZeroCon19',
         'ada25',
         'Accessible', 'IDPD2019', 'neverwashingmycheek', 'g4ebootcamp',
         'FutureDecoded', 'A11y', 'Hamiltunes', 'axschat',
         'deafgain', 'SBLIV', 'HLAA2016',
         'AutismAdvantage',
         'IT', 'RisingLeaders', 'SeeAmazing', 'Pride2017',
         'SCOTUS',
         'wheelchairinmotion', 'inspiration', 'GnomeLastedFiveMinutes',
         'MicrosoftAI', 'Obama', 'ADA', 'InclusiveDesign',
         'Blind',
         'ATIA19', 'PartiallySighted',
         'EdRobertsDay', 'JustDoIt', 'USBLN', 'Skype', 'accessibilty',
         'inclusivehiring', 'SignLanguageWeek', 'ADA27',
         'abilityhack',
         'CSUNATC18', 'BritAbroadDrama', 'WAAD', 'LA2015',
         'ndcautism16', 'SCNYC17',
         'WorldAutismAwarenessDay', 'accessible', 'disabilityisastrength',
         'hackathon', 'DeafProblems', 'GAAD',
         'disability', 'cfasummit', 'MSIgnite', 'socialgood', 'EyeMine',
         'AwesomeAintEasy', 'access', 'USBLN17', 'Dreamers',
         'Build2017', 'autismatwork',
         'noexcuse', 'X019', 'IWDeaf2018',
         'NonVisibleDisabilities', 'Disability', 'MicrosoftEDU',
         'Disabilities', 'InsiderFast', 'USBLN18',
         'inclusionworks', 'individuality', 'CSUNATC17',
         'ImagineCup', 'tech',
         'AccessibilityTips', 'wheelchair', 'MinecraftEDU', 'Gamescom2019',
         'business', 'HitRefresh', 'empowering', 'cfa16', 'cpchat',
         'TEDTalk',
         'xboxa11y', 'SpecialOlympics', 'E2',
         'deaffriendly',
         'IronMan', 'October1st', 'WHChamps', 'bobbi4GU', 'innovation',
         'SBLIII', 'worldbrailleday', 'lead', 'Invention', 'PSBJCorpCit',
         'WAAD2015', 'autism',
         'MicrosoftEvent',
         'WindowsTip', 'AbilityAward', 'ALSicebucketchallenge', 'WinHEC',
         'Outlook', 'DesignForAll', 'MostAdmired', 'HoloLens',
         'pALS', 'Gameon', 'a11ycampseattle', 'PR',
         'Neurodiversity', 'code', 'Paralympics', 'Bett2018',
         'GleasonMovie',
         'DigitalInclusion', 'microsoft', 'LearningTools', 'GLEASON',
         'AssistiveTechnology', 'jobs', 'DisabilityConfident',
         'TeamGleason',
         'USBLN2015', 'PWA', 'neurodiverse', 'InclusionAward',
         'AbilityWeek',
         'NewTenPoundNote',
         'MSFTSummit', 'CSUNATC19', 'DisAbility', 'DigitalTransformation',
         'NFBWATD', 'likeadyslexic',
         'DeepLearning', 'nowhiteflags', 'TEDxGlasgow2015', 'trust',
         'OfficeforCats', 'linus', 'CBeebies', 'Tech4GoodAwards', 'CSUN18',
         'GAconf', 'BillyT', 'EdTech', 'nonprofits', 'sxsw',
         'GoHawks', 'ForbesUnder30', 'WSD2017', 'SXSW2019', 'fail',
         'DeafAwarenessMonth', 'WoV15', 'msignite2017', 'Apple',
         'WorldStandardsDay', 'IDPD', 'MsIgnite', 'lovemyjob', 'MIEExpert',
         'AltText', 'accessibility', 'rword', 'Word', 'Sundance', 'SOTU',
         'ADA25', 'InternationalLiteracyDay', 'AmericanSignLanguage',
         'ally',
         'AGT',
         'TheFeed', 'NDEAM', 'MicrosoftStream', 'MicrosoftTeams', 'PSA',
         'edchat', 'Braille', 'HKAA18', 'mentalhealthtreatment',
         'aprilfoolsday', 'ignite2017', 'CSUN', 'MondayMotivation',
         'Minecraft',
         'employment',
         'a11y', 'SeattlePride', 'WomensMarchSeattle', 'Microsoft',
         'AgainstAllOdds', 'inclusive', 'windows',
         'VivaTech',
         'IWD2017', 'AutismAtWork', 'SurfacePro', 'ID24',
         'DisabilityAnswerDesk', 'Johnscrazysocks', 'hardofhearing',
         'AACAwarenessMonth', 'StrikeOutALS', 'HumanRightsDay',
         'AutismAwarenessMonth', 'aoda', 'WIRED25', 'teamgleason',
         'Ability2016', 'SkypeTranslator', 'SXSW', 'BillyTNinjacat',
         'edtech',
         'Redmond', 'InclusiveEducation', 'Nominations', 'abilitysummit',
         'InternationalDisabilityDay', 'MVPSummit', 'CommunityStory',
         'ImmersiveReader',
         'grateful', 'UpgradeYourWorld', 'GlobalAccessibilityAwarenessDay',
         'SmartCities', 'InclusionInAction', 'CSUN16', 'windowsinsider',
         'InclusivetheFilm', 'learningtools', 'PurpleTuesday', 'IDPD2015',
         'EUAccessCity', 'Inclusivethefilm', 'hearingloss', 'loveit',
         'disabilityinclusion',
         }

victor = {'a11yourdays', 'Accessibility', 'a11y', 'GAAD', 'a11ycast',
          'accessiblecurrency', 'cerebralPalsy', 'InspiredBySound', 'ARlab',
          'speechrec', 'webdev', 'accessibility', 'a11yTOCamp',
          'DisabledCompliments', 'w4a2019', 'GAAD2018', 'A11yClub',
          'Firefox', 'softwareengineer', 'NVDA', 'google', 'A11y',
          'android', 'webdesign', 'w4a2017', 'Chrome', 'NFB17', 'Talkback',
          'Android', 'csunatc19', 'svg', 'GAAD2017', 'aira', 'csun17',
          'NFB18', 'GAAD2019', 'Harvey', 'inclusive', 'blind', 'LyreBird',
          'CSUNATC17', 'AudioDescription', 'Audible', 'a11yTech',
          'Year4Audio', 'CSUNATC19', 'SoftwareEngineer', 'fail', 'ACB18',
          'XLNAudio', 'Breaking', 'GoogleArts', 'TechItOut', 'web', 'id24u',
          'forms', 'InaccessibilityMeans', 'io19', 'deletefacebook', 'ux',
          'GoogleHome', 'Intellectsoft', 'edtech', 'accessible', 'deaf',
          'TalkBack', 'wordpress', 'androiddev', 'apps', 'CSUNATC18', 'dev',
          'MicrosoftSupportVideo', 'UX', 'AppleVisPodcast', 'dyslexia'}

molly = {'disability', 'blindpeopleproblems', 'blindsnaps',
         'disabilityonyoutube', 'disabilityofYT', 'blindgirlbeauty',
         'worldsightday', 'Beyond2020Vision', 'blindgirlpower',
         'thingsblindgirlssay', 'disabilitiesonYT',
         'disabilitiesonyoutube', 'blindgirlstorytime',
         'accessibilitymatters', 'blindgirl', 'disabilityonYT',
         'GuideDogs', 'blindgirlproblems', 'blindgirlmoments', 'Blind',
         'accessibility', 'GuideDog', 'blindgirlwin', 'blind',
         'servicedog', 'blindgirlWIN', 'blindgirlinsta', 'deaf', 'Braille',
         'inclusion'}

print("Common between all three:")
print(jenny.intersection(victor.intersection(molly)))
print()
print("Common between jenny and victor:")
print(jenny.intersection(victor))
print()
print("Common between jenny and molly:")
print(jenny.intersection(molly))
print()
print("Common between victor and molly:")
print(victor.intersection(molly))

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

set4 = jenny.intersection(victor.intersection(molly))
fin = ', '.join(set4)

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=set(STOPWORDS),
                      min_font_size=10,
                      color_func=random_color_func).generate(fin)

plt.figure(figsize=(20, 10), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
