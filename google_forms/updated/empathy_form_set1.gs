function createEmpathyEvaluationForm_Set1() {
  // Create form
  var form = FormApp.create('Empathy Evaluation - Set 1');
  
  // Add instructions
  form.setDescription(
    'Please evaluate the following conversations between a user and a chatbot. ' +
    'Rate each conversation on four dimensions of empathy using the scale provided.\n\n' +
    'Scale: 0 = Not at all, 1 = Somewhat, 2 = Strongly present'
  );
  
  // Add conversations
  
  // Conversation 1
  form.addPageBreakItem()
    .setTitle('Conversation 1');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 1')
    .setHelpText(conversationData['conv_1'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 2
  form.addPageBreakItem()
    .setTitle('Conversation 2');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 2')
    .setHelpText(conversationData['conv_2'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 3
  form.addPageBreakItem()
    .setTitle('Conversation 3');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 3')
    .setHelpText(conversationData['conv_3'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 4
  form.addPageBreakItem()
    .setTitle('Conversation 4');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 4')
    .setHelpText(conversationData['conv_4'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 5
  form.addPageBreakItem()
    .setTitle('Conversation 5');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 5')
    .setHelpText(conversationData['conv_5'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 6
  form.addPageBreakItem()
    .setTitle('Conversation 6');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 6')
    .setHelpText(conversationData['conv_6'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 7
  form.addPageBreakItem()
    .setTitle('Conversation 7');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 7')
    .setHelpText(conversationData['conv_7'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 8
  form.addPageBreakItem()
    .setTitle('Conversation 8');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 8')
    .setHelpText(conversationData['conv_8'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 9
  form.addPageBreakItem()
    .setTitle('Conversation 9');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 9')
    .setHelpText(conversationData['conv_9'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 10
  form.addPageBreakItem()
    .setTitle('Conversation 10');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 10')
    .setHelpText(conversationData['conv_10'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 11
  form.addPageBreakItem()
    .setTitle('Conversation 11');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 11')
    .setHelpText(conversationData['conv_11'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 12
  form.addPageBreakItem()
    .setTitle('Conversation 12');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 12')
    .setHelpText(conversationData['conv_12'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 13
  form.addPageBreakItem()
    .setTitle('Conversation 13');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 13')
    .setHelpText(conversationData['conv_13'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 14
  form.addPageBreakItem()
    .setTitle('Conversation 14');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 14')
    .setHelpText(conversationData['conv_14'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 15
  form.addPageBreakItem()
    .setTitle('Conversation 15');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 15')
    .setHelpText(conversationData['conv_15'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 16
  form.addPageBreakItem()
    .setTitle('Conversation 16');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 16')
    .setHelpText(conversationData['conv_16'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 17
  form.addPageBreakItem()
    .setTitle('Conversation 17');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 17')
    .setHelpText(conversationData['conv_17'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 18
  form.addPageBreakItem()
    .setTitle('Conversation 18');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 18')
    .setHelpText(conversationData['conv_18'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 19
  form.addPageBreakItem()
    .setTitle('Conversation 19');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 19')
    .setHelpText(conversationData['conv_19'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 20
  form.addPageBreakItem()
    .setTitle('Conversation 20');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 20')
    .setHelpText(conversationData['conv_20'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 21
  form.addPageBreakItem()
    .setTitle('Conversation 21');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 21')
    .setHelpText(conversationData['conv_21'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 22
  form.addPageBreakItem()
    .setTitle('Conversation 22');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 22')
    .setHelpText(conversationData['conv_22'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 23
  form.addPageBreakItem()
    .setTitle('Conversation 23');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 23')
    .setHelpText(conversationData['conv_23'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 24
  form.addPageBreakItem()
    .setTitle('Conversation 24');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 24')
    .setHelpText(conversationData['conv_24'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 25
  form.addPageBreakItem()
    .setTitle('Conversation 25');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 25')
    .setHelpText(conversationData['conv_25'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 26
  form.addPageBreakItem()
    .setTitle('Conversation 26');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 26')
    .setHelpText(conversationData['conv_26'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 27
  form.addPageBreakItem()
    .setTitle('Conversation 27');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 27')
    .setHelpText(conversationData['conv_27'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);

  // Conversation 28
  form.addPageBreakItem()
    .setTitle('Conversation 28');
  
  form.addSectionHeaderItem()
    .setTitle('Conversation 28')
    .setHelpText(conversationData['conv_28'].text);
  
  // Emotional Reactions
  form.addMultipleChoiceItem()
    .setTitle('Emotional Reactions')
    .setHelpText('Does the bot express warmth, compassion, or concern?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Explorations  
  form.addMultipleChoiceItem()
    .setTitle('Explorations')
    .setHelpText('Does the bot attempt to explore the user\'s experiences and feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Interpretations
  form.addMultipleChoiceItem()
    .setTitle('Interpretations')
    .setHelpText('Does the bot communicate understanding of the user\'s experiences?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
    
  // Overall Empathy
  form.addMultipleChoiceItem()
    .setTitle('Overall Empathy')
    .setHelpText('Did the bot demonstrate understanding of the user\'s feelings?')
    .setChoiceValues(['0 - Not at all', '1 - Somewhat', '2 - Strongly present'])
    .setRequired(true);
  
  // Log form URL
  Logger.log('Form URL: ' + form.getPublishedUrl());
  Logger.log('Edit URL: ' + form.getEditUrl());
}

var conversationData = {
  'conv_1': {
    text: "Bot: Hi there! 😊 Just checking in to see how you\'re doing with integrating those small activity breaks into your day. Remember, even a little movement can make a big difference! Let me know how it\'s going or if you need any tips. Keep up the great work! 💪🌟\n\nUser: Working well.  I have been making little changes to look for ways to move throughout the day and I feel better physically and mentally\n\nBot: Great to hear that you\'ve been able to make those changes and are feeling better. Were you able to take those short breaks to stretch or walk, or maybe pace during calls? How did those activities go for you?\n\nUser: Yes!  I did all those things with some fequency, and they helped take my mind away from my job stress for a few minutes while getting my blood flowing.  All good!\n\nBot: Glad to hear that those activities were beneficial. Do you feel you need any adjustments to your current plan to stay active, or is it working well for you as it is?\n\nUser: I think working well—I just want to be more consistent with it\n\nBot: To enhance consistency, consider setting reminders or scheduling specific times for those breaks. This should help reinforce the routine. Let me know if you want to add anything else to your plan.\n\nUser: Sounds good, thank you\n\nBot: You\'re welcome! Just checking in—how are you feeling overall? Are you still managing stress well with your new routine? If you need any tips or support, I\'m here to help!\n\nUser: My stess level has lowered a bit due to working in these little activities—it’s been a nice side benefit\n\nBot: It\'s wonderful to hear that you\'ve found relief through little activities! To keep the good vibes going, try watching some funny animal videos—they\'re great for a quick mood boost. Here\'s a link to get you started: [Funny Animal Videos](https://www.youtube.com/results?search_query=funny+animal+videos). On a scale of 1 to 10, how helpful was this suggestion? Please also share how it made you feel or any other thoughts you have about it.\n\nUser: Yep, funny animal videos are always fun\n\nBot: I\'m glad to hear you enjoy funny animal videos! They can be a great way to lighten the mood. It sounds like you\'re making wonderful progress with your physical activity and managing stress. If you ever need more tips or support, feel free to reach out. Keep up the great work, and take care! Goodbye for now! 😊",
    participant_id: "whatsapp:+15745494036",
    session: "current_session",
    round: "round_2",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_2': {
    text: "User: Hi\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: I am absolutely fine\n\nBot: I\'m glad to hear that! Before we move on, I\'d be interested in knowing more about you so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: I am a 34 old doctor who works for an average of 45 hours a week\n\nBot: Thank you for sharing that. It sounds like you have quite a busy schedule! What are some things that make you happy or help you recharge after your workdays? For example, some people enjoy experiencing nature, reading a good book, listening to music, or hanging out with friends.\n\nUser: maybe taking a small walk or riding a bicycle.\n\nBot: Those sound like great ways to unwind and recharge! How would you describe the environment you are living in? Is it in a city, or a rural area? This might help us find more opportunities for incorporating those activities into your routine.\n\nUser: I am living in a city\n\nBot: Living in a city can offer some unique opportunities for staying active, like biking paths or parks for walking. Now, let\'s focus on figuring out what\'s been holding you back from being more active. Common barriers can include things like lack of time, social support, motivation, energy, financial resources, neighborhood safety, family obligations, weather, or fear of injury. What do you think has been holding you back?\n\nUser: Family obligations and motivation\n\nBot: Thank you for sharing that. Balancing family obligations with self-care can definitely be challenging, and finding motivation is something many people struggle with. Do you think stress is a significant barrier to more physical activity for you?\n\nUser: no\n\nBot: That\'s helpful to know. Let’s explore some ways to work around the barriers you mentioned. For instance, instead of setting aside a lot of extra time for exercise, how do you feel about finding small opportunities throughout your day to add steps?\n\nUser: I am okay with it\n\nBot: Great! Some small opportunities might include taking a quick walk during your lunch break, pacing while you’re on a phone call, or parking a bit farther away when running errands. These small actions can add up without needing a big time commitment. \n\nWhat\'s your typical day like? Perhaps we can identify some potential opportunities where you can fit in a bit more activity.\n\nUser: I am a health practitioner soo most of the time i am dealing with patients.\n\nBot: Being a health practitioner means you\'re likely on your feet a lot already, which is a great start. You might consider incorporating short walks or stretches between patient appointments, taking the stairs instead of the elevator when possible, or doing a few minutes of light exercises during breaks. How do you feel about giving these ideas a try?\n\nUser: Its a nice idea. I am going to give it a trial\n\nBot: That\'s wonderful to hear! Let\'s think about what benefits being more active might bring to your life. For example, improving your mood, boosting energy levels, building self-confidence, enhancing body image, managing weight, reducing stress and depression, enhancing overall physical health, or even improving sleep quality and creating opportunities to meet new people. Which of these benefits resonates with you the most?\n\nUser: boosting energy levels\n\nBot: Boosting energy levels is a fantastic and very motivating benefit! On a scale of 0 to 10, how important is having more energy to you?\n\nUser: having some energy makes me feel motivated.\n\nBot: That\'s great to hear, and it\'s important to recognize that having more energy can positively impact many areas of your life. Now, after considering everything we\'ve discussed, what actions do you plan to try in the next 7 days to become more physically active? For example, the small opportunities we discussed earlier might be a good starting point.\n\nUser: Alright. Thank you for the insights.\n\nBot: You\'re very welcome! Just to help you keep on track, how confident do you feel, on a scale of 0 to 10, about implementing these actions in the next 7 days?\n\nUser: 9\n\nBot: That\'s a high level of confidence, and that\'s fantastic to hear! It sounds like you\'re ready to take these steps towards becoming more active. I\'ll follow up with you around this time every two days to check in and see how things are going. Sound good?",
    participant_id: "whatsapp:+254791338758",
    session: "session_1",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_3': {
    text: "User: EXP\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: Hi\n\nBot: Before we move on, I\'d be interested in knowing more about you so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: Hi, I am doing great. Pleasure meeting you.\n\nBot: The pleasure is mine! So, how do you usually unwind after work?\n\nUser: After work, i usually do some light exercises like jogging. Sometimes, i do some interesting things like watching a movie.\n\nBot: That sounds great! Engaging in light exercises like jogging is a wonderful way to unwind. Watching a movie can also be a nice way to relax. What are some things that make you happy or help you recharge? For example, some people enjoy experiencing nature, reading a good book, listening to music, or hanging out with friends.\n\nUser: A good question. Basking on the beaches is one of the things that usually make me happy. It breaks boredom.\n\nBot: Basking on the beaches sounds refreshing and revitalizing! It\'s wonderful that you have an activity that brings you happiness and helps break boredom. How would you describe the environment you are living in? Is it in a city, or a rural area?\n\nUser: I live in a suburban area.\n\nBot: Living in a suburban area often provides a nice balance of space and access to nature. Now, as we discuss adding more physical activity into your routine, what do you think has been holding you back from being more active? For example, common barriers include lack of time, social support, motivation, energy, and financial resources. Other concerns might be neighborhood safety, family obligations, weather, or fear of injury.\n\nUser: Great question. My main barrier is limited time. My work at times takes more time leaving me with little to just have peace with myself.  Financial constraints is another challenge.\n\nBot: I understand how limited time and financial constraints can be significant barriers to staying active. It can be challenging to balance work commitments with personal well-being. Do you think stress is a significant barrier to more physical activity for you as well?\n\nUser: Not really. I rarely have stress.\n\nBot: That\'s good to hear! So let\'s explore some ways to work around the time and financial constraints. Instead of setting aside a lot of extra time, how do you feel about finding small opportunities throughout your day to add steps? For example, you could take a quick walk during your lunch break, pace while you’re on a phone call, or park a little farther away when running errands. These small steps can add up without needing a big time commitment. How does that sound to you?\n\nUser: Wow! This sounds great.\n\nBot: I\'m glad you think so! Let\'s take a closer look at your regular day. Could you walk me through a typical day, and we can identify some potential opportunities to incorporate these small activities?\n\nUser: I just get out of my home headed to my workplace in the morning untill evening.\n\nBot: Thanks for sharing that with me. Given your routine, maybe you could try taking a brisk walk before heading to work or during your lunch break. If possible, taking the stairs instead of the elevator can also be a quick way to add some activity. How do you feel about trying these out?\n\nUser: These are better options. Infact, there is no an elevator where I work.\n\nBot: That\'s great, as taking the stairs is a simple way to add some physical activity to your day. Now, considering these options, what kinds of benefits do you think being more active might bring to your life? Feel free to ask me if you need some examples.\n\nUser: Good health and immunity boosting.\n\nBot: Those are excellent benefits! Regular physical activity can indeed lead to better overall health and a stronger immune system. On a scale of 0 to 10, how important are these benefits to you?\n\nUser: 9\n\nBot: That\'s quite high on the importance scale, which is fantastic! It\'s great to see how much you value health and immunity. At this point, after reviewing all of this, what actions do you plan to give a try in the following 7 days to be more physically active? We\'ve discussed some small opportunities like taking brisk walks and using the stairs.",
    participant_id: "whatsapp:+254769432017",
    session: "session_1",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_4': {
    text: "Bot: Hi [User\'s Name]! 😊 Just checking in on your progress with incorporating more walking into your routine. How\'s it going so far? Remember, every step counts! 🚶‍♀️🚶‍♂️ Let me know if you need any extra motivation or tips. Keep it up! 🙌\n\nUser: Thanks I am trying my best but sometimes time is limited\n\nBot: How have you been these past two days?\n\nUser: Intense work is increasing so it means walking more faster and regularly\n\nBot: How did your plan for physical activity go? Did you get a chance to walk more as planned?\n\nUser: Yes\n\nBot: When you were doing the physical activity, how did you feel emotionally?\n\nUser: I was drained but kept on since I can\'t just walk out of work\n\nBot: Understood. Let\'s update your action plan for physical activity if needed. Would you like to adjust your walking routine or explore other options?\n\nUser: Yes\n\nBot: Consider shorter, more frequent walks during breaks or incorporating walking meetings. FINISHED.\n\nUser: Sure I will\n\nBot: Acknowledged.\n\nUser: Yes\n\nBot: Understood.\n\nUser: Okay\n\nBot: Noted.",
    participant_id: "whatsapp:+254727709702",
    session: "current_session",
    round: "round_2",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_5': {
    text: "User: Hi\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: I’m okay how about yourself?\n\nBot: I\'m doing well, thank you! Before we move on, I\'d be interested in knowing more about you so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: I usually just go and sit down on the couch or lay down and later I go outside to my backyard and play with my kids\n\nBot: That sounds like a nice balance between relaxation and spending quality time with your kids. What are some other things that make you feel happy or recharged? For example, some people enjoy experiencing nature, reading a good book, listening to music, or hanging out with friends.\n\nUser: I think just spending time with family is what makes me happy. I like playing sports with my kids.\n\nBot: That\'s wonderful to hear! It seems like family and being active with your kids already brings you joy. How would you describe the environment you are living in? Is it in a city, or rural area?\n\nUser: It’s in a city\n\nBot: Great, that gives me a better picture of your surroundings. What do you think has been holding you back from being more active? Common barriers include lack of time, social support, motivation, energy, or financial resources. There could also be concerns like neighborhood safety, family obligations, weather, or fear of injury.\n\nUser: I think lack of motivation and lack of time as well\n\nBot: Those are very common challenges, and you\'re definitely not alone in feeling that way. Do you think stress is a significant barrier to more physical activity for you as well?\n\nUser: I would think so but it’s not a huge barrier\n\nBot: I understand. Let\'s explore some ways to work around the lack of motivation and time. Instead of needing a big time commitment, how do you feel about finding small opportunities throughout your day to add steps? For instance, taking a quick walk during your lunch break, pacing while you’re on a phone call, or parking a little farther away when running errands can be helpful. Do any of these ideas resonate with you, or do you have other small activities in mind?\n\nUser: I think the parking further away wouldn’t be too bad that way I can get more steps in. I think also playing some sports with my children would allow me to move around some more\n\nBot: Those sound like great opportunities to incorporate more activity into your day naturally. How do you feel about giving these a try?\n\nUser: I don’t mind doing it I just have to remember to do it because I might forget and end up parking closer or I might not be motivated to go outside and play some sports. It’s just the motivation that gets to me.\n\nBot: I understand, and it\'s completely normal to feel that way. Motivation can be tricky, but sometimes setting small reminders can help. You might try setting an alarm on your phone or placing a note somewhere visible to remind you to park a bit farther or schedule playtime with your kids. \n\nLet\'s talk about the benefits of being more active and how they might motivate you. What kinds of benefits do you think being more active might bring to your life? Feel free to ask if you need some examples.\n\nUser: Yeah that’s true maybe I should put a sticky note somewhere on my cars dashboard to remind me and yeah can you give me some examples?\n\nBot: Absolutely! Being more active can improve your mood, boost your energy levels, build self-confidence, and enhance your body image. It can also help with weight management and reduce mental health concerns such as stress and depression. Additionally, regular physical activity enhances overall physical health and reduces the risk of diseases such as cancer, cardiovascular disease, and diabetes. It often improves sleep quality and can bring opportunities to meet new people through group activities or even just walking around your neighborhood. \n\nDo any of these benefits resonate with you?\n\nUser: Of course I think just the health aspect resonates with me a lot because obviously I want to live a long life to be able to see my kids grow up. I think just feeling more confident in myself seeing how I lose weight and gain muscle will make a difference.\n\nBot: Those are excellent and meaningful reasons to be more active. On a scale of 0 to 10, how important is it to you to experience these benefits, particularly the health aspect and self-confidence?\n\nUser: 10\n\nBot: That\'s fantastic to hear! It sounds like these benefits are very important to you and serve as strong motivation. Considering everything we\'ve discussed so far, what actions do you plan to try in the next 7 days to be more physically active? We\'ve talked about parking further away and playing sports with your kids. Are there any other activities you\'d like to include?\n\nUser: I think I might try to work out more in my home whether it be push ups or crunches or using dumb bells. I also would probably like to get a gym membership so I can force myself to go and work out and maybe tag along with some friends.\n\nBot: Those sound like excellent steps towards increasing your physical activity. Working out at home with push-ups, crunches, or dumbbells is a great start, and getting a gym membership could not only boost your motivation but also provide a social aspect if you bring friends along. On a scale of 0 to 10, how confident are you in doing these actions in the next 7 days?\n\nUser: 8\n\nBot: An 8 is a great confidence level to start with! It sounds like you\'re pretty motivated and have some excellent strategies in place. I\'ll check in around this time every two days to see how things are going. Remember, it\'s all about small steps and finding what works best for you. If anything comes up or you want to adjust your plan, feel free to let me know. You\'ve got this!\n\nUser: Sounds great I’ll see you in 2 days.\n\nBot: Perfect, looking forward to our next check-in. Take care and good luck with your new activities! Remember, small steps lead to big changes. See you in two days!",
    participant_id: "whatsapp:+15094261432",
    session: "session_1",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 2
    }
  },
  'conv_6': {
    text: "Bot: Hey there! Just checking in—how are the short walks or workouts going after work? Let me know if there\'s anything I can help with or adjust. 😊\n\nUser: Well the walks are working. The past 2 days have been really rough at work so I couldn\'t squeeze in a small workout. The walks are really helping with my headspace!\n\nBot: I\'m sorry to hear work has been tough, but it\'s wonderful that the walks are helping clear your mind. It sounds like they\'re really beneficial for you. Would you like to revisit your goals to see if there\'s anything we can tweak to make things a bit easier?\n\nUser: Sure thing\n\nBot: It\'s great to hear that the walks are helping with your headspace. You\'re doing a fantastic job by taking that step for yourself, especially with a rough work schedule. Would you like to focus more on the walks for now, or is there another activity you\'d like to try incorporating?\n\nUser: At the moment the walks are probably the number 1 focus. I\'m thinking about yoga but I cannot commit to it yet.\n\nBot: Focusing on the walks sounds like a solid plan, especially since they\'re already making a positive impact. It\'s great that you\'re considering yoga too, even if you\'re not ready to dive in just yet. It seems like you\'re open to exploring new activities at your own pace. How does that feel for you?\n\nUser: It feels great. A year or two ago I wouldn\'t have even considered walking outside at all. Hearing the birds chirp and smelling the fresh air is helping with my stress levels a lot.\n\nBot: It\'s fantastic to hear how much you\'re enjoying the outdoors and how it\'s helping with your stress. Would you like to take a look at your goals to make sure they continue to support your well-being?\n\nUser: Sure thing\n\nBot: Let\'s take a look at your goals to make sure they align with your well-being and stress management. How does that sound?\n\nUser: Yes\n\nBot: It sounds like you\'re really benefiting from your walks, which is fantastic. Would you like to set a specific goal, like walking a certain number of days each week, or would you prefer to keep things flexible for now?\n\nUser: I would like to set a goal of walking for 15 minutes 5 times a week.\n\nBot: That sounds like a great goal! Walking for 15 minutes, five times a week, is a wonderful way to keep up with your progress and manage stress. Is there anything else you\'d like to add or adjust to your plan?\n\nUser: No I think this goal will help me feel confident enough in a couple weeks to start branching out and bring more goals into my daily life.\n\nBot: That sounds like a fantastic approach. You\'re setting yourself up for success by choosing a goal that\'s both achievable and confidence-building. I\'m really impressed with your plan to gradually incorporate more goals into your daily life. Is there anything else you\'d like to discuss or need support with?\n\nUser: There is nothing else. You have been a tremendous help! Thank you!\n\nBot: I\'m so glad to hear that! It\'s inspiring to see how you\'re setting yourself up for success. Your progress is truly encouraging. Before we wrap up, how are you feeling overall? Are you managing your stress well, or is there anything else on your mind that you\'d like to talk about? Remember, I\'m here to support you whenever you need it!\n\nUser: My stress levels have been lowered, but are still there. I think if I keep this going I will be set up for success.\n\nBot: It\'s great to hear your stress levels have decreased! Watching funny animal videos can be a delightful way to further lift your mood and ease stress. Here\'s a link to get started: [Funny Animal Videos](https://www.youtube.com/results?search_query=funny+animal+videos). On a scale of 1 to 10, how helpful was this suggestion? Please also share how it made you feel or any other thoughts you have about it.\n\nUser: 5. I need a more physical approach to decrease my stress.\n\nBot: I appreciate your honesty! It sounds like you\'re looking for more physical activities to help manage your stress, which aligns perfectly with your walking goal. Staying active is a great way to keep those stress levels in check. I\'m really proud of the progress you\'re making, and I believe that sticking to your walking plan will set you up for even more success. \n\nIf you ever want to explore more activities or need support, just reach out. Take care, and I look forward to hearing about your progress next time! Goodbye for now! 😊",
    participant_id: "whatsapp:+12679710379",
    session: "current_session",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_7': {
    text: "User: Hi\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: I am doing pretty good\n\nBot: I\'m glad to hear that! Before we move on, I\'d be interested in knowing more about you so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: I usually get my house straight and I clean a bit, then I go to my gym for a bit some days and do some light workouts. After that I usually play video games or take a nap.\n\nBot: That sounds like a good mix of activities you enjoy. It\'s great that you already incorporate some workouts into your routine. What are some things that make you happy or recharged? For example, some people enjoy experiencing nature, reading a good book, listening to music, or hanging out with friends.\n\nUser: I like playing story games or watching my favorite shows or youtubers.\n\nBot: Those sound like enjoyable ways to relax and recharge. How would you describe the environment you’re living in? Is it in a city, or a rural area?\n\nUser: Rural\n\nBot: Living in a rural area can offer its own unique opportunities and challenges for physical activity. Let\'s talk about what might be holding you back from being more active. Common barriers include lack of time, social support, motivation, energy, and financial resources. Other concerns can be neighborhood safety, family obligations, weather, or fear of injury. What do you think has been holding you back?\n\nUser: I think that a diet change is needed, I have a sensitive stomach and often times I will eat and it makes my stomach hurt so I don\'t have the motivation to get up and do anything.\n\nBot: It sounds like your sensitive stomach and diet play a significant role in your motivation and ability to be active. That can certainly be challenging. Do you feel that stress is also a significant barrier to being more physically active, or is it mainly the dietary issues?\n\nUser: Sometimes it can be, I think that stress can make me also not want to get up and do things.\n\nBot: It\'s understandable how stress, along with diet-related issues, can impact your motivation to be active. Let\'s explore some ways to work around these barriers. Instead of setting aside a lot of extra time, how do you feel about finding small opportunities throughout your day to add steps? For instance, you could take a quick walk during a break at home, pace while you’re on a phone call, or perhaps do some light stretching or exercises while watching your favorite shows or videos. What do you think of these ideas?\n\nUser: I think the walks sound great or just getting an in home walking pad or treadmill.\n\nBot: Those are excellent ideas! Incorporating short walks or using a walking pad or treadmill at home can be very practical and manageable ways to increase physical activity. How do you feel about giving these options a try?\n\nUser: I would try them\n\nBot: That\'s great to hear! Let\'s talk about the positive changes that being more active might bring to your life. What kinds of benefits do you think being more active might offer you? Feel free to ask me if you need some examples.\n\nUser: I think it could help be more fit and give me more confidence\n\nBot: Those are wonderful benefits to look forward to. Improving fitness and building self-confidence can indeed have a positive impact on various aspects of life. On a scale of 0 to 10, how important are these benefits to you?\n\nUser: 8\n\nBot: That\'s a solid level of importance. Those benefits can really motivate you on your journey towards being more active. With that in mind, what actions do you plan to try in the next 7 days to increase your physical activity? We\'ve discussed options like short walks or using a walking pad or treadmill at home.\n\nUser: Walk more and eat a bit better\n\nBot: That sounds like a great plan! Focusing on walking more and making some dietary improvements can work hand in hand to boost your overall well-being. On a scale of 0 to 10, how confident are you in your ability to follow through with these actions over the next 7 days?\n\nUser: 8\n\nBot: That\'s a good level of confidence to start with. It sounds like you’re ready to take some positive steps forward. I will follow up with you around this time of day every two days to check in and see how things are going. Feel free to reach out if you have any questions or need support in the meantime. You\'ve got this!\n\nUser: ok\n\nBot: Great! I look forward to our next check-in. Take care, and remember to enjoy the process at your own pace. See you soon!",
    participant_id: "whatsapp:+13363019854",
    session: "session_1",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_8': {
    text: "Bot: Hey there! Just checking in to see how things are going with parking further away and playing sports with the kids. Have you had the chance to add any home workouts or think more about the gym membership? Remember, small steps add up! 😊🚶‍♂️🏃‍♀️💪\n\nUser: Yes so I’ve been parking further away getting more steps in and I’ve been playing basketball with my kids and soccer so I’m running around more now. I also started workouts at home I’ve been working out 30 minutes minimum about 5 days a week. I’m still contemplating the gym because price is a factor but so far so good.\n\nBot: That\'s awesome! It sounds like you\'re really making progress by getting more steps in and staying active with your kids. Plus, committing to those home workouts is impressive. I totally get being cautious about the gym membership cost, and you\'re doing great with what you have. How have you been feeling emotionally while doing these activities?\n\nUser: I’ve been feeling really good. I feel like I have more energy when I wake up and I feel much more self confident. I feel like my body is starting to feel better as the days go by.\n\nBot: That\'s wonderful to hear! It sounds like you\'re truly experiencing the positive effects of being more active, both physically and emotionally. Having more energy and confidence is such a great motivator. Do you feel good about sticking with your current plan, or is there anything you\'d like to tweak or add to your routine?\n\nUser: No I think the current plan is good like I said at some point I will buy the gym membership but for now this will do. I think I am feeling much better than I was the other days. I am also eating healthier too.\n\nBot: It\'s wonderful to hear that you\'re feeling better and making healthier eating choices. You\'re truly on a great path, and it\'s clear your efforts are paying off. I understand waiting on the gym membership until it feels right for you. Keep up the amazing work! Is there anything else you\'d like to discuss or any other support you need?\n\nUser: Not that I can think of at the moment.\n\nBot: I\'m really glad to hear that you\'re feeling better and making such positive changes. Your dedication to staying active and eating healthier is truly inspiring. It\'s perfectly okay to take things one step at a time, and you\'re doing a fantastic job with what you have. If you ever need support or have questions in the future, don\'t hesitate to reach out. Keep up the great work! FINISHED.\n\nUser: Thank you for the motivation and I’ll keep trying!\n\nBot: You\'re doing an amazing job by staying committed to your goals and making positive changes in your life. It\'s great to hear that you\'re feeling more energetic and confident. If you\'d like, we can review your goals together to make sure you\'re on track and feeling supported.\n\nUser: Sure that sounds great\n\nBot: Great! Let\'s take a moment to review your goals. You\'re parking further away, staying active with your kids through sports, and committing to home workouts five days a week. You\'re also thinking about a gym membership down the line and focusing on healthier eating. Does this capture your current goals, or is there anything you\'d like to tweak or add?\n\nUser: That captured everything thank you\n\nBot: You\'re doing an amazing job balancing everything and making these positive changes. It\'s clear you\'re dedicated to your health and well-being, and that\'s truly commendable. Keep up the fantastic work, and remember, I\'m here to support you whenever you need it. FINISHED.",
    participant_id: "whatsapp:+15094261432",
    session: "current_session",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 1,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_9': {
    text: "User: Hi\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: I\'m good!\n\nBot: That\'s great to hear! Before we move on, I\'d be interested in knowing more about you so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: I am currently not employed at the moment but I do enjoy playing some video games or watching some shows\n\nBot: Thank you for sharing that with me. Video games and shows can be a great way to relax! What are some other things that make you happy or help you recharge? For example, some people enjoy experiencing nature, reading a good book, listening to music, or hanging out with friends.\n\nUser: I enjoy listening to music!\n\nBot: Listening to music is such a wonderful way to lift your mood and recharge. Thank you for sharing that with me. How would you describe the environment you are living in? Is it in a city, or a rural area?\n\nUser: I live in the city\n\nBot: Living in the city offers so many opportunities for exploration. With that in mind, what do you think has been holding you back from being more active? Common barriers include lack of time, social support, motivation, energy, or financial resources. Sometimes, other concerns such as neighborhood safety, family obligations, weather, or fear of injury can also be factors.\n\nUser: Motivation.. I pretty much stay home to grind out supplementary income so I can\'t afford to go out much\n\nBot: I understand how focusing on generating income can make it hard to find motivation for other activities. It sounds like you\'re really dedicated to your work at home, and that\'s admirable. Do you think stress is a significant barrier to more physical activity for you?\n\nUser: financial stress perhaps\n\nBot: Financial stress can indeed be a significant factor, and it\'s understandable how it might impact your motivation to engage in activities outside the home. Let’s explore some ways to work around these barriers. For example, instead of setting aside extra time or incurring costs, how do you feel about finding small opportunities throughout your day to add steps? These can be simple and free. For instance, taking a quick walk during a break, pacing while you’re on a phone call, or even incorporating some movement while listening to music. What do you think about these options?\n\nUser: Yeah that sounds like some solid options. I can always just take a 15 minute break to just walk around the neighborhood\n\nBot: That sounds like a great plan! It\'s amazing how even a short, 15-minute walk can provide a nice break and add some movement into your day. Since you enjoy listening to music, you could bring your favorite playlist along for an enjoyable walk. How do you feel about giving that a try?\n\nUser: Yea that sounds great!\n\nBot: I\'m glad to hear that! It sounds like you\'re open to exploring new possibilities. Thinking about stepping into physical activity, what kinds of benefits do you think being more active might bring to your life? Feel free to ask me if you need some examples.\n\nUser: It makes me feel more healthier I would assume\n\nBot: Absolutely, feeling healthier is a significant benefit of being more active, and it can encompass so many aspects, from improving your overall physical health to boosting your mood and energy levels. On a scale of 0 to 10, how important does this benefit of feeling healthier mean to you?\n\nUser: Definitely a 10\n\nBot: That\'s wonderful to hear that feeling healthier is so important to you! At this point, after reviewing everything we\'ve discussed, what actions do you plan to try in the next 7 days to be more physically active? For example, we have discussed taking a 15-minute walk around your neighborhood while listening to music.\n\nUser: I plan to take a break throughout the day and spend that time walking around the neighborhood. I can also look into other options like the gym with a friend\n\nBot: Those sound like fantastic plans! Incorporating walks and considering the gym with a friend can be a great way to stay motivated and make the experience more enjoyable. On a scale of 0 to 10, how confident are you in doing these actions in the next 7 days?\n\nUser: Hmm.. I would say a solid 7 just because I\'m starting it out\n\nBot: That\'s a great starting point! Feeling a bit uncertain when trying something new is completely normal, and you\'re already taking a huge step by planning to try it. I will follow up with you around this time of day every two days to check in and see how everything is going. Does that sound good to you?\n\nUser: yea!\n\nBot: Great! I\'m looking forward to hearing how your new routines work out for you. Remember, it\'s all about taking small steps and finding what feels enjoyable for you. If you need any support or have questions along the way, feel free to reach out. Enjoy your walks and the music!\n\nUser: Thanks!\n\nBot: You\'re welcome! Have a wonderful day, and enjoy your time exploring these new activities. Take care!\n\nUser: See ya!\n\nBot: See you! Take care and talk soon!",
    participant_id: "whatsapp:+13127090097",
    session: "session_1",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_10': {
    text: "Bot: Hey there! How\'s it going with those brisk walks and taking the stairs? 😊 Have you had a chance to enjoy any outdoor activities lately? Let me know if you need any more ideas to stay active! 🏃‍♀️🌳\n\nUser: It is just wow! I cant fail to say thank you.\n\nBot: I\'m thrilled to hear that! It sounds like you\'re really making the most of your opportunities to stay active. How have the past two days been for you? Have you been able to follow through with your physical activity plan?\n\nUser: Yes, sure. I have followed every bit of it and i can confiem to you that I am seeing tangible results on my end.\n\nBot: That\'s fantastic to hear! You\'re doing an amazing job sticking to your plan, and it\'s great that you\'re already noticing results. How did you feel emotionally while you were engaging in those activities?\n\nUser: I felt motivated to do even more. It is just enjoyabe.\n\nBot: I\'m thrilled to hear that you\'re feeling motivated and enjoying the activities! It sounds like you\'re really embracing this positive change, and that\'s fantastic. Since you\'re seeing such great results, is there anything you\'d like to tweak or add to your physical activity plan?\n\nUser: Those ones are enough for now.\n\nBot: You seem really motivated and happy with your current routine, which is fantastic. It\'s great that you\'ve found a balance that works for you. If you ever want to try something new or make any changes, just let me know. Keep up the great work! FINISHED.\n\nUser: I surely will. Thank you for your support.\n\nBot: You\'re very welcome! It\'s inspiring to see your commitment to staying active, and it\'s clear that your efforts are making a difference. Keep up the great work, and remember, I\'m here to support you whenever you need it. FINISHED.\n\nUser: Pleasure\n\nBot: It\'s truly a pleasure to support you on this journey. You\'re doing an amazing job, and it\'s wonderful to hear how motivated and enjoyable you find your activities. Keep up the great work, and feel free to reach out anytime you need support or want to share your progress. FINISHED.\n\nUser: Fine\n\nBot: It\'s great to hear how well you\'re doing with your physical activity plan and the results you\'re seeing. Your dedication is truly inspiring. If there\'s anything else you\'d like to explore or talk about, just let me know. I\'m here to help. FINISHED.\n\nUser: Okay.Thank you\n\nBot: You\'re very welcome! It\'s fantastic to see your commitment and enjoyment in your physical activity journey. If you ever want to chat or explore new ideas, feel free to reach out. I\'m here to support you. FINISHED.",
    participant_id: "whatsapp:+254769432017",
    session: "current_session",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_11': {
    text: "User: Hi\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: Hey! I\'m feeling a bit lazy on this rainy Wednesday but doing good.\n\nBot: I\'m glad to hear you\'re doing well, even if the weather is making things a bit sluggish. Before we move on, I\'d be interested in knowing more about you, so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: I usually crack open a cold beer and play some video games on my computer. Either that or watch some Netflix.\n\nBot: That sounds like a relaxing way to destress after a long day. What are some things that make you happy or recharged? For example, some people enjoy experiencing nature, reading a good book, listening to music, or hanging out with friends.\n\nUser: Usually to recharge I will hang out with my friends and cook up some good food. We like to play corn hole, ping pong, and darts also!\n\nBot: That sounds like a lot of fun and a great way to stay social and active! How would you describe the environment you are living in? Is it in a city, or a rural area?\n\nUser: I live in the suburbs at the moment so a mix of both.\n\nBot: That sounds like a great place with a balance of tranquility and accessibility. Let\'s delve a bit deeper. What do you think has been holding you back from being more active? Some common barriers include lack of time, social support, motivation, energy, and financial resources. Other concerns might be neighborhood safety, family obligations, weather, or fear of injury.\n\nUser: The main 3 things holding me back are motivation, energy levels and family obligations.\n\nBot: I hear you on those challenges. They can definitely make it hard to fit in more activity. Do you think stress is a significant barrier to more physical activity for you as well?\n\nUser: 100% yes. How can I feel motivated and determined if I\'m constantly stressing.\n\nBot: It\'s completely understandable that stress can sap energy and motivation. Let\'s explore some ways to work around these barriers. How do you feel about finding small opportunities throughout your day to add a bit of movement, even if it\'s just for a few minutes at a time? These can be less daunting than dedicating a large chunk of time.\n\nUser: In theory that sounds great but it doesn\'t always work out like that in reality.\n\nBot: I understand; it can be challenging to integrate new habits into your existing routine. Maybe we can brainstorm together to fit these small opportunities more seamlessly into your day. Some examples could include taking a quick walk during your lunch break, pacing while you\'re on a phone call, or even taking a few extra steps around the house. What does your regular day look like, and could we identify any potential moments to add a little movement?\n\nUser: My usual workday involves heavy lifting and constant cleaning as I work in the rental industry. I could add a walk or some light workouts when I get off work though.\n\nBot: That\'s great! It sounds like your job already involves a decent amount of movement. Adding a short walk or some light exercises after work could help you unwind and boost your energy level without overexerting yourself. How do you feel about trying those out when you finish your shift?\n\nUser: I can give it a try for a couple days and see how it works out, can\'t see it hurting only helping.\n\nBot: That sounds like a positive approach. What kinds of benefits do you think being more active might bring to your life? Feel free to ask if you need some examples.\n\nUser: More confidence in myself, less time to stress or worry think.\n\nBot: Those are great benefits to aim for. On a scale of 0 to 10, how important are these benefits to you?\n\nUser: 10 out of 10\n\nBot: That\'s wonderful to hear! At this point, after reviewing all of this, what actions do you plan to give a try in the following 7 days to be more physically active? For example, we talked about maybe going for a walk or doing some light workouts after work.\n\nUser: The most reasonable plan would be to either take a 10 to 15 minute walk after work, or take 15 minutes out of my time out of work to stretch and get some push-ups or situps in.\n\nBot: That sounds like a solid plan that fits well with your routine. On a scale of 0 to 10, how confident are you in doing these actions in the following 7 days?\n\nUser: I would say a solid 6\n\nBot: A 6 is a good starting point! It\'s great that you\'re willing to give this a try. Remember, any effort is progress, and it\'s about finding what feels right for you. I will follow up with you around this time every two days to check in!\n\nUser: Sounds good. Thank you!\n\nBot: You\'re welcome! I\'m here to support you, and I look forward to hearing about your progress. Don\'t hesitate to reach out if you have any questions or need a bit of encouragement. Have a wonderful rest of your day!",
    participant_id: "whatsapp:+12679710379",
    session: "session_1",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 2
    }
  },
  'conv_12': {
    text: "Bot: Hey there! 😊 Just checking in on how your physical activity is going. Have you had a chance to enjoy any outdoor activities in your area lately? Let me know how you\'re doing! 🏞️🚶‍♀️\n\nUser: Yes, I just went on a walk today for about an hour.\n\nBot: That\'s wonderful! It\'s great that you took some time for a walk today. How have the past couple of days been for you overall?\n\nUser: Pretty good! Had a nice weekend to cool off.\n\nBot: I\'m glad to hear you had a nice weekend to unwind. It sounds like you\'re doing a great job balancing relaxation and activity. How did your plan for physical activity go over the past two days? Did you get a chance to try anything else besides walking?\n\nUser: They went great! I kept up on my walks and have been increasing my daily steps.\n\nBot: That\'s fantastic! You\'re really making strides by increasing your daily steps and staying consistent with your walks. How have you been feeling emotionally while doing these activities?\n\nUser: I have been feeling better emotionally, I think the walks help with my anxiety.\n\nBot: I\'m really glad to hear that your walks are helping with your anxiety. It\'s amazing how being active can boost our mood and well-being. You\'re doing a fantastic job taking care of yourself. Do you feel like your current routine is working well, or would you like to explore any new activities?\n\nUser: I think it is working well.\n\nBot: I\'m glad to hear your routine is working well for you. It\'s important to find what makes you feel good and stick with it. Do you feel comfortable continuing with your current plan, or is there anything you\'d like to tweak or add?\n\nUser: I think I will continue with my current plan\n\nBot: That sounds like a solid plan! It\'s great that you\'ve found a routine that works for you. If you ever want to revisit your goals or need any support, feel free to reach out. Keep up the great work!\n\nUser: Thanks!\n\nBot: You\'re welcome! If you ever want to chat about how your activities are affecting your mood or if you have new goals in mind, I\'m here for you. How do you feel about sticking with your current routine for now?",
    participant_id: "whatsapp:+16613610080",
    session: "current_session",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_13': {
    text: "User: Hi\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: Doing quite well, thank you.  How are you?\n\nBot: I\'m doing well, thanks for asking! Before we move on, I\'d be interested in knowing more about you so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: When I get home from work, I thank God for a good day at work and for getting home safely, then I kiss my wife, pet my dogs, change into workout clothes and work out for about an hour, typically.\n\nBot: That sounds like a wonderful routine and a great way to unwind! It\'s impressive that you already have a workout routine. Since you enjoy spending time with your wife and your dogs, what are some other activities that make you feel happy or recharged? For example, some people find joy in experiencing nature, reading a good book, listening to music, or hanging out with friends.\n\nUser: First and foremost, I enjoy and find deep fulfillment in prayer and studying the Bible and practicing my Catholic faith.  I also enjoyed exercising outside in nature whenever I can.  I like reading all types of books, from history to novels, and I listen to music often—when I work out, when I drive home, etc.  I also enjoy keeping connected with my family and friends as much as I can.\n\nBot: Those are all wonderful activities that bring a lot of balance and joy into life. It sounds like your faith, family, and being in nature are incredibly important to you. How would you describe the environment you are living in? Is it in a city, or a rural area?\n\nUser: I live in a quiet suburb near a mid-sized Midwestern city.\n\nBot: Living in a quiet suburb sounds peaceful and it sounds like you have some opportunities to enjoy nature close by. Let\'s shift our focus slightly. What do you think has been holding you back from being even more active, if that\'s something you\'re interested in? Common barriers include lack of time, social support, motivation, energy, or sometimes just the unpredictability of life.\n\nUser: For ne, it is probably a combination of being busy with lots of responsibilities and sometimes motivation—my job is stressful and sometimes I don’t feel like even starting a workout.\n\nBot: I understand, balancing responsibilities with finding time to be active can be challenging. Stress can certainly take a toll on motivation. Do you think stress might be a significant barrier to more physical activity for you at times?\n\nUser: Yes, it might be the biggest\n\nBot: Thank you for sharing that with me. Stress can indeed be a significant obstacle. Let’s explore some ways to work around this barrier. For instance, instead of trying to set aside a lot of additional time, how would you feel about finding small opportunities throughout your day to add more physical activity? There are ways we can integrate movement that don\'t require a big time commitment.\n\nUser: Yes, that could be useful to me\n\nBot: Great! Some small opportunities might include taking a quick walk during your lunch break, pacing while you’re on a phone call, or parking a little farther away when running errands. These small steps can add up over time. What does your regular day look like, and do you think there might be potential opportunities for you to incorporate some of these movements?\n\nUser: My regular day at the office consists of being at my desk a lot and participating in meetings on the computer and working on the computer\n\nBot: In that case, you might consider integrating short breaks to stretch or walk a bit within your workspace. Perhaps standing or pacing during phone calls and using breaks to step outside for a quick walk could help. Even getting up every hour to move around for a few minutes can be beneficial. How do you feel about giving some of these a try?\n\nUser: Yes, could definitely give these a try, they all seem feasible for me\n\nBot: That\'s wonderful to hear! Let\'s talk about why being more active might be beneficial for you. What kinds of benefits do you think being more active could bring to your life? Feel free to ask if you need some examples or ideas.\n\nUser: I think movement is key to staying healthy, so being moref active by keeping myself moving I think would help me feel more healthy and lower my stress and anxiety and help me feel less stiff\n\nBot: Those are excellent reasons! Physical activity is indeed a crucial component of staying healthy and can certainly help in reducing stress and anxiety while keeping you feeling more flexible. On a scale of 0 to 10, how important do you feel these benefits are to you?\n\nUser: At least a 9!\n\nBot: That\'s great to hear that these benefits are so important to you! At this point, after reviewing all of this, what actions do you plan to give a try in the following 7 days to be more physically active? We\'ve discussed some small opportunities like stretching, taking short walks, or pacing during calls. Are there any specific actions you\'re thinking of incorporating into your routine?",
    participant_id: "whatsapp:+15745494036",
    session: "session_1",
    round: "round_2",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_14': {
    text: "Bot: Hey there! 😊 Just checking in to see how your efforts to sneak in those extra steps and stretches are going. Have you had a chance to explore any new biking paths or parks this week? Let me know how it\'s going! 🚴‍♂️🌳 Keep up the good work! 💪\n\nUser: yes\n\nBot: That\'s awesome! It sounds like you\'re really taking advantage of the opportunities around you. How have the past couple of days been for you overall?\n\nUser: Its been awesome,  i feel motivated to do more and more exercise\n\nBot: That\'s fantastic to hear! It\'s great that you\'re feeling motivated. Were you able to fit in those short walks, stretches, or take the stairs as we talked about?\n\nUser: Yes\n\nBot: That\'s fantastic! It sounds like you\'re really making progress. How did you feel emotionally while doing these activities?\n\nUser: very jovial\n\nBot: That\'s wonderful to hear! Exercise can really lift your spirits and boost your energy. Since things are going so well, do you feel like you want to update or add anything to your action plan for physical activity?\n\nUser: No. I think I am okay with the previous recommendation.\n\nBot: You\'re doing an amazing job sticking to your plan and finding joy in your activities. Your motivation and positive attitude are truly commendable. Keep up the great work, and remember, I\'m here to support you whenever you need it. Is there anything else you\'d like to discuss or any questions you have?\n\nUser: You are much welcome. Right now i don\'t have any other question.\n\nBot: Thank you for sharing your progress with me. It\'s wonderful to hear that you\'re feeling motivated and joyful with your activities. If you\'re happy with your current goals, that\'s great! But if you ever want to revisit them or need any support, I\'m here for you. Keep up the fantastic work!\n\nUser: Alright, Thank you\n\nBot: You\'re very welcome! I\'m glad to hear things are going well. If you ever want to revisit your goals or need any adjustments, just let me know. Keep up the great work, and take care!\n\nUser: Alright\n\nBot: I\'m really glad to hear that you\'re feeling motivated and enjoying your physical activities. Your positive attitude and dedication are truly inspiring. If you ever want to try something new or need any support, I\'m here for you. Keep up the fantastic work! FINISHED.",
    participant_id: "whatsapp:+254791338758",
    session: "current_session",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_15': {
    text: "Bot: Hey! 😊 How are your walks going? Have you been able to find some moments to enjoy the beautiful surroundings? Let me know if there\'s anything I can do to support you! 🌟🚶‍♂️\n\nUser: Good let\'s pretend the two days have passed.\n\nBot: Hi there! How have the past couple of days been for you? Were you able to fit in some walks or maybe check out the gym like we talked about? 😊\n\nUser: Yeah I went on walks with my mom haven\'t gone to the gym yet though.\n\nBot: That\'s fantastic that you got to enjoy some walks with your mom! How did you feel emotionally during those walks? 😊\n\nUser: Felt very good and peaceful.\n\nBot: I\'m really happy to hear that your walks were so peaceful and enjoyable. It sounds like you\'re truly embracing the beauty around you and cherishing the time with your mom. That\'s great progress! 🌟\n\nSince you haven\'t made it to the gym yet, would you like to tweak your action plan, or do you feel ready to give it another shot soon? 😊\n\nUser: No, I will probably go once I am good financially when I give it a shot.\n\nBot: I completely understand waiting until you\'re in a better financial spot before trying out the gym. It\'s important to prioritize, and it\'s wonderful that you\'re staying active with your walks. Taking things one step at a time is perfectly okay. 😊\n\nIs there anything else you\'d like to adjust or add to your plan for now, or are you happy to keep focusing on the walks? 🌿🚶‍♂️\n\nUser: Nothing that I can think of.\n\nBot: That sounds great! It seems like you\'re on a good path with your walks. Before we wrap up, how are you feeling overall? Are you experiencing any stress or anything on your mind that you\'d like to talk about? I\'m here to help if you need it! 😊\n\nUser: I feel pretty good, a little bit of stress. But beyond that pretty good.\n\nBot: I\'m glad to hear you\'re feeling pretty good! To help ease that little bit of stress, watching some funny animal videos can be a great mood booster. Here\'s a link to get you started: [Funny Animal Videos](https://www.youtube.com/results?search_query=funny+animal+videos). \n\nOn a scale of 1 to 10, how helpful was this suggestion? Please also share how it made you feel or any other thoughts you have about it.\n\nUser: I would say a 10 made me laugh a little. And I\'m sure it would help others.\n\nBot: I\'m so glad to hear that the funny animal videos made you laugh! Laughter is a great way to relieve stress. 😊 \n\nIt sounds like you\'re doing well with your walks and finding peace in nature, which is wonderful. If you ever feel like discussing more ways to manage stress or any other activities, I\'m here for you. \n\nTake care, and I look forward to hearing about your next walks! Have a great day! 🌟🚶‍♂️\n\nUser: Thanks, you aswell.\n\nBot: Thank you! 😊 It sounds like you\'re doing really well with your walks and finding those peaceful moments. If you\'d like to go over your goals together, I\'m here to help, but if you\'re feeling good about your current plan, that\'s great too! 🌿🚶‍♂️\n\nUser: Thanks!\n\nBot: You\'re very welcome! 😊 It sounds like you\'re doing a fantastic job by taking steps toward being more active, and it\'s perfectly okay to go at your own pace. I just wanted to check in—are you feeling stressed about anything in particular, or is it more of a general feeling? Remember, you\'re not alone in feeling a bit stressed sometimes. Keep enjoying those walks and the peaceful moments they bring. If you ever want to chat more about your goals or anything else, I\'m here for you. Take care! 🌟",
    participant_id: "whatsapp:+18628813389",
    session: "current_session",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 2,
      explorations: 2,
      interpretations: 1,
      empathy: 2
    }
  },
  'conv_16': {
    text: "Bot: Hi there! 😊 Just checking in—how’s your walking detour going? Any new discoveries on the way home, or adjustments needed? Keep up the amazing work! 💪🚶‍♂️📚\n\nUser: I started taking a detour to do a more scenic route and that felt good\n\nBot: That\'s great to hear! It sounds like you\'re really enjoying the scenic route. How did it make you feel emotionally while you were walking?\n\nUser: I liked it, it made me feel lighter?\n\nBot: It sounds like the scenic route is really lifting your spirits. Feeling lighter is such a wonderful benefit of being active. You\'re doing a fantastic job incorporating this into your routine! Would you like to revisit your goals or make any updates to your action plan?\n\nUser: No it\'s okay\n\nBot: I\'m glad to hear that you\'re happy with your current plan. If you ever want to explore new activities or revisit your goals, just let me know. Keep enjoying those walks and the lighter feeling they bring! Is there anything else you\'d like to talk about or any other support you need?\n\nUser: Nope all good\n\nBot: I\'m really glad to hear that everything\'s going well! Just checking in—are you feeling any stress lately, or is everything feeling pretty good? If you ever want to chat about your goals or need any support, I\'m here for you. Enjoy your walks and the positivity they bring! Take care!\n\nUser: Okay thank you\n\nBot: I understand you\'re going through a tough time. Watching funny animal videos is a great way to lift your spirits and relieve stress. Here\'s a list to get you started: [Funny Animal Videos](https://www.youtube.com/results?search_query=funny+animal+videos). On a scale of 1 to 10, how helpful was this suggestion? Please also share how it made you feel or any other thoughts you have about it.",
    participant_id: "whatsapp:+14045280621",
    session: "session_2",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 1,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_17': {
    text: "User: Hi\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: I am doing pretty good! Just came back from an hour walk with my friend.\n\nBot: That\'s wonderful to hear! It sounds like you\'re already finding some time for physical activity, which is great. Before we move on, I\'d be interested in knowing more about you so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: I usually go on a walk with my friend.\n\nBot: That sounds like a fantastic way to unwind and catch up with your friend. I\'m glad you\'re already incorporating some physical activity into your routine. What are some other things that make you happy or help you recharge? For example, some people enjoy experiencing nature, reading a good book, listening to music, or hanging out with friends.\n\nUser: I like talking to my friend on the computer, playing games, or doing surveys online to make some extra cash.\n\nBot: Those sound like enjoyable activities that help you unwind and even offer a bit of extra income. It\'s great that you find ways to relax and connect with your friend virtually. How would you describe the environment you are living in? Is it in a city, or a rural area?\n\nUser: I live in a pretty big suburb.\n\nBot: Thanks for sharing that with me. Suburbs can sometimes offer a nice balance of residential neighborhoods and accessible parks or walking areas. Let\'s focus a bit on physical activity. What do you think has been holding you back from being more active? For example, common barriers include lack of time, social support, motivation, energy, and financial resources. Other concerns might be neighborhood safety, family obligations, weather, or fear of injury.",
    participant_id: "whatsapp:+16613610080",
    session: "session_1",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_18': {
    text: "Bot: Hi there! 😊 Just checking in to see how your scenic walks have been going. Hope those funny animal videos are still keeping your spirits high too! Let me know if there\'s anything you\'d like to chat about. Take care! 🌟\n\nUser: I\'ve been doing some more scenic walks so that\'s good\n\nBot: That\'s wonderful to hear! Scenic walks can really lift the spirits. How have the past two days been for you overall?\n\nUser: Pretty good actually, although I\'ve been quite busy\n\nBot: It\'s great that you\'ve managed to fit in your scenic walks despite being busy. That shows real dedication! How did your plan for physical activity go? Were you able to enjoy those walks as you intended?",
    participant_id: "whatsapp:+14045280621",
    session: "session_3",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_19': {
    text: "Bot: Hey there! 😊 Just checking in—how have the hourly stretch breaks been going? Any progress on fitting that 30-min weight lifting into your routine? Remember, every bit counts! Let me know how you’re feeling. 💪\n\nUser: Hello!\n\nBot: Hi there! I hope you\'re doing well. How have the past couple of days been for you, especially when it comes to fitting in some physical activity?\n\nUser: I am doing good. I started to commit myself to 30 minutes a day. I am building the routine.\n\nBot: That\'s great to hear! How\'s it been going so far? Are you noticing any changes in your energy or motivation levels?\n\nUser: I feel sore! But generally I feel more neutral. Not as sluggish or tired.\n\nBot: I understand that feeling sore can be a bit uncomfortable, but it\'s a sign that your body is adapting to the new routine. It\'s great to hear that you\'re not feeling as sluggish or tired. That\'s a positive change! How did you feel emotionally while you were doing the physical activity?\n\nUser: I didn\'t dwell on it. I just got through and did it. The workout was exhausting.\n\nBot: It\'s impressive that you pushed through, even when it felt exhausting. That shows a lot of determination and commitment. Do you feel like this routine is sustainable for you, or would you like to tweak your action plan to make it more manageable?\n\nUser: I believe I can make it work! I just have to stick with it.\n\nBot: That\'s great to hear! Your confidence in sticking with it is a strong motivator. Staying committed, even when it\'s challenging, is key. Is there anything else you\'d like to adjust or add to your plan to help you stay on track?\n\nUser: I believe my plan is perfect for me right now. What suggestions would you make if I want to adjust in the future?\n\nBot: It\'s great that your plan feels right for you at the moment. If you decide to make changes in the future, you could try mixing up the activities to keep things fresh, or adjusting the duration and intensity based on your energy levels. It\'s perfectly normal to adapt your routine as you go to better suit your needs. Is there anything else you\'d like to talk about or explore?\n\nUser: No, I think that is it! Thank you so much.\n\nBot: You seem really motivated and committed, which is fantastic. If you ever want to tweak your plan or just chat about your progress, I\'m here to support you. Keep up the great work, and take care! FINISHED.\n\nUser: You too! Bye.\n\nBot: Take care, and feel free to reach out anytime you need support or want to chat about your progress. Bye!",
    participant_id: "whatsapp:+19188108927",
    session: "current_session",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_20': {
    text: "User: Hi\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: Good\n\nBot: I\'m glad to hear that. Before we move on, I\'d be interested in knowing more about you so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: I usually watch tv\n\nBot: That sounds like a classic way to relax. What are some other things that make you happy or help you feel recharged? For example, some people enjoy experiencing nature, reading a good book, listening to music, or hanging out with friends.\n\nUser: Going for a walk\n\nBot: Going for a walk can be a wonderful way to unwind and enjoy some fresh air. How would you describe the environment you are living in? Is it in a city, or a rural area?\n\nUser: Downtown  big city\n\nBot: Living downtown in a big city definitely has its unique vibe and energy. Now, let\'s shift our focus a bit. What do you think has been holding you back from being more active? For example, common barriers include lack of time, social support, motivation, energy, and financial resources. Other concerns can be neighborhood safety, family obligations, weather, or fear of injury.\n\nUser: Motivation pain. Back pain\n\nBot: I understand; dealing with back pain can certainly make it challenging to feel motivated to be active. Do you think stress plays a role as a significant barrier to more physical activity for you as well?\n\nUser: Yes but I am not sure how\n\nBot: Thank you for sharing that. Stress can sometimes impact motivation and how we experience pain, making everything feel a bit more challenging. Let’s explore some ways to work around these barriers. For example, rather than setting aside lots of time, how would you feel about finding small opportunities throughout your day to add steps?\n\nUser: Sure what are your ideas\n\nBot: Here are a few ideas that might fit into your day: you could take a short walk during your lunch break, pace while you’re on a phone call, or park a little farther away when running errands. These small steps could add up without needing a big time commitment. What does a regular day look like for you, and we can see where you might find similar opportunities?\n\nUser: I spend most of the day working on a computer\n\nBot: In that case, perhaps you could try standing up and stretching every hour or so, or even do a quick walk around the office or your home. If you\'re making phone calls, consider walking around during those conversations. How do you feel about giving some of these small changes a try?\n\nUser: Yes I could do that\n\nBot: That\'s great to hear! Let\'s delve a bit deeper into the potential benefits. What kinds of positive changes do you think being more active could bring to your life? If you\'d like some examples, feel free to ask.\n\nUser: Less pain?\n\nBot: Absolutely, regular movement can indeed help manage and even reduce back pain over time by strengthening muscles and improving flexibility. On a scale of 0 to 10, how important is reducing your pain to you?\n\nUser: 9\n\nBot: That\'s quite important for you. Reducing your pain can make a significant difference in your daily life and overall well-being. Since this is a high priority for you, what actions do you plan to take in the next 7 days to be more physically active? We\'ve discussed some small opportunities you could try, like taking short breaks to stretch or walk around your workspace.\n\nUser: Stretching and walking more\n\nBot: That sounds like a good plan to start with. On a scale of 0 to 10, how confident are you about being able to incorporate stretching and walking into your routine over the next week?\n\nUser: 6\n\nBot: A 6 is a solid starting point. It\'s great to see that you\'re willing to try. Are there any adjustments or additional support that might help increase your confidence in following through with these actions?\n\nUser: I get distracted or side tracked easily. Cell phone reminders\n\nBot: Setting cell phone reminders can be a helpful way to stay on track and keep you mindful of your goals throughout the day. I\'ll follow up with you around this time of day every two days to check in on how things are going. How does that sound?\n\nUser: Great\n\nBot: Excellent! I\'m really glad to hear that. Remember, the aim here is to take small steps towards making physical activity a part of your daily routine. If you ever have any questions or need more support, feel free to reach out. I\'m looking forward to catching up in a couple of days. Take care!\n\nUser: It\'s been 2 days I have not heard from you\n\nBot: Hi there! I apologize for the delay in reaching out. I\'m glad to hear from you though. How have the past two days been regarding the stretching and walking activities we talked about?\n\nUser: I have been pretty good about walking more. Not perfect\n\nBot: That\'s wonderful to hear! It\'s great that you\'ve made progress in walking more, and remember, it\'s perfectly okay not to be perfect. Every step counts. Have you had any challenges or noticed any changes in how you\'re feeling since you started?",
    participant_id: "whatsapp:+16123868977",
    session: "session_1",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 2
    }
  },
  'conv_21': {
    text: "Bot: Hey there! Just checking in 😊 How\'s everything going with your walking and diet changes? Let me know how you\'re feeling! 💪🚶‍♂️🥗\n\nUser: I have started to go to the gym in my building more often and I have incorperated fruits into my diet instead of sweets\n\nBot: That\'s fantastic! Swapping sweets for fruits is a great choice, and hitting the gym more often shows real dedication. You\'re making wonderful progress! How have you been feeling emotionally when you\'re at the gym or making these dietary changes?\n\nUser: I feel like I am getting fit, lifestyle changes for the better always feel good.\n\nBot: That\'s wonderful to hear! It\'s fantastic that you\'re feeling the benefits of your positive changes. It sounds like you\'re really committed to improving your lifestyle. How do you feel about your progress so far? Is there anything you\'d like to adjust or add to your action plan for physical activity?\n\nUser: I think we should start slow for now, I can add some more goals in the next few days\n\nBot: That sounds like a smart plan. Taking it slow and gradually building up is a great way to make sure these changes stick. You\'re definitely on the right path. Is there anything specific you\'d like to focus on, or any challenges you think might come up in the next few days?\n\nUser: I would like to lose a few pounds\n\nBot: It\'s great that you\'re setting goals for yourself, and wanting to lose a few pounds is both common and achievable. You\'re already making excellent progress with your gym visits and dietary changes. Keep up the fantastic work! Is there anything specific you\'d like to explore or try to support your weight loss journey?\n\nUser: Not at the moment my current plan is to go slow and steady\n\nBot: That sounds like a wise approach. Slow and steady progress is often the most sustainable and rewarding. You\'re doing a fantastic job by taking these steps and being mindful of your pace. Keep it up! If you ever want to explore new ideas or need support, I\'m here for you. Is there anything else you\'d like to discuss or tweak in your plan right now?\n\nUser: Nope\n\nBot: I see you\'re happy with your current plan and want to maintain your steady progress, which is fantastic! Just checking in—how are you feeling overall? Are you experiencing any stress or challenges as you work towards your goals? If anything comes up or you need support, I\'m here for you. Keep up the great work, and don\'t hesitate to reach out anytime!\n\nUser: Im feeling good\n\nBot: I\'m glad to hear you\'re feeling good! Watching funny animal videos can be a great way to lift your mood even more. Here\'s a list to enjoy: [Funny Animal Videos](https://www.youtube.com/results?search_query=funny+animal+videos). On a scale of 1 to 10, how helpful was this suggestion? Please also share how it made you feel or any other thoughts you have about it.\n\nUser: 2\n\nBot: I\'m glad to hear you\'re feeling good! It sounds like you\'re making some positive changes, and that\'s really encouraging. If you ever want to explore new ideas or need support, I\'m here for you. \n\nAs you continue on your journey, remember to take it slow and steady, just like you mentioned. If you have any questions or need to chat, don’t hesitate to reach out. \n\nTake care, and keep up the great work! Goodbye for now! 😊\n\nUser: bye\n\nBot: I\'m really glad to hear you\'re feeling good! It sounds like you\'re on a positive path with your lifestyle changes. Just checking in—are you experiencing any stress or challenges as you work towards your goals? If there\'s anything else you\'d like to discuss or any support you need, feel free to reach out. Take care, and keep up the great work!",
    participant_id: "whatsapp:+13363019854",
    session: "current_session",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_22': {
    text: "User: Hi\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: Am fine how about you?\n\nBot: I\'m doing well, thank you. Before we move on, I\'d be interested in knowing more about you so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: Mostly relax and talk with my friend\n\nBot: Understood. What are some things that make you happy or recharged? For example, some people enjoy experiencing nature, reading a good book, listening to music, or hanging out with friends.\n\nUser: Listening to music and movies, hanging out with friends and reading a good book\n\nBot: Noted. How would you describe the environment you are living in? Is it in a city, or rural area?\n\nUser: City suburbs\n\nBot: What do you think has been holding you back from being more active? Common barriers include lack of time, social support, motivation, energy, and financial resources. Other concerns include neighborhood safety, family obligations, weather, and fear of injury.\n\nUser: Lack of time and motivation\n\nBot: Do you think stress is a significant barrier to more physical activity for you?\n\nUser: No\n\nBot: Let’s explore some ways to work around these barriers. Instead of setting aside a lot of extra time, how do you feel about finding small opportunities throughout your day to add steps? For example, taking a quick walk during your lunch break, pacing while you’re on a phone call, or parking a little farther away when running errands. These small steps add up without needing a big time commitment. What does your regular day look like, and can you identify any potential opportunities?\n\nUser: Since my work is in a hospital setting i usually walk around a lot which has helped me\n\nBot: Noted. How do you feel about continuing to incorporate those walks into your routine?\n\nUser: I feel confident that I can achieve more walking with proper motivation\n\nBot: What kinds of benefits do you think being more active might bring to your life? Examples include improving mood, boosting energy, building self-confidence, enhancing body image, helping with weight management, reducing mental health concerns, enhancing physical health, and reducing disease risk. Which resonate with you?\n\nUser: My main concern is weight management but I also believe regular exercise cn improve my energy and body image\n\nBot: On a scale of 0 to 10, how important are these benefits to you?\n\nUser: 10\n\nBot: Noted. At this point, what actions do you plan to try in the next 7 days to be more physically active? We\'ve discussed incorporating more walking into your routine.\n\nUser: Incorporating more walking\n\nBot: On a scale of 0 to 10, how confident are you in doing this in the next 7 days?\n\nUser: 7\n\nBot: I will follow up with you around this time every two days to check in.\n\nUser: Okay. Thanks\n\nBot: Understood. Goodbye.",
    participant_id: "whatsapp:+254727709702",
    session: "session_1",
    round: "round_2",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_23': {
    text: "User: Hi\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: Hello, how are you?\n\nBot: I\'m doing well, thank you for asking! Before we move on, I\'d be interested in knowing more about you so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: I usually unwind after work by getting a nice meal or maybe even going on a jog.\n\nBot: That sounds like a great way to relax and take care of yourself. It\'s wonderful that you incorporate jogging into your routine as a form of unwinding. What are some things that make you happy or recharged? For example, some people enjoy experiencing nature, reading a good book, listening to music, or hanging out with friends.\n\nUser: Nature definitely makes me feel relaxed. Aswell as listening to music.\n\nBot: Nature and music are both fantastic ways to recharge and find peace. They can also be wonderful companions for physical activity, like a walk or jog. How would you describe the environment you are living in? Is it in a city, or rural area?\n\nUser: It\'s a rural area.\n\nBot: Living in a rural area can provide beautiful surroundings for outdoor activities and opportunities to connect with nature. Now, as we focus more on enhancing your physical activity, what do you think has been holding you back from being more active? For example, common barriers include lack of time, social support, motivation, energy, and financial resources. Other concerns include neighborhood safety, family obligations, weather, and fear of injury.\n\nUser: Definitely, financial resources and lack of motivation.\n\nBot: I understand how financial resources and motivation can be challenging obstacles. It\'s important to recognize that these are common feelings, and finding manageable ways to incorporate activity is key. Do you think stress is a significant barrier to more physical activity for you?\n\nUser: Stress definitely creates a barrier for me.\n\nBot: Thank you for sharing that with me. Stress can indeed make it more challenging to stay motivated for physical activity. Let’s explore some ways to work around these barriers. For example, instead of setting aside a lot of extra time, how do you feel about finding small opportunities throughout your day to add steps?  \n\nSome ideas might include taking a quick walk during your break, pacing while on a phone call, or parking a little farther away when running errands. These small steps add up without needing a big time commitment. What does a regular day look like for you, and how do you feel about trying these small opportunities?\n\nUser: Usually I will walk with my mom and that will help alot.\n\nBot: Walking with your mom sounds like a wonderful way to add some activity and enjoy each other\'s company. It\'s great that you have that social support. How do you feel about trying to incorporate more of those small opportunities like your walks throughout your week?\n\nUser: I feel pretty good since it helps a lot.\n\nBot: That\'s awesome to hear! Since walking seems to really work for you, let\'s consider the potential benefits of being more active. What kinds of benefits do you think being more active might bring to your life? Feel free to ask if you need some examples.\n\nUser: Maybe going to the gym?\n\nBot: Going to the gym is a great option if it\'s feasible and you\'re interested. It can offer a variety of equipment and classes to suit different interests and fitness levels. In addition, regular physical activity like going to the gym can improve your mood, boost your energy levels, and enhance your overall health. Which of these potential benefits resonate with you the most?\n\nUser: Improving my energy levels so I can do more.\n\nBot: Improving your energy levels is a fantastic goal and can lead to being more productive and engaged in your daily activities. On a scale of 0 to 10, how important is this benefit to you?\n\nUser: 10\n\nBot: That’s a strong level of importance, which is wonderful! Improving your energy levels can have a positive impact on many aspects of your life. Considering everything we\'ve discussed, what actions do you plan to give a try in the following 7 days to be more physically active? For example, we have discussed some small opportunities, like incorporating more walks with your mom and possibly visiting the gym if it\'s accessible.\n\nUser: I can\'t really think of anything beyond that.\n\nBot: That\'s perfectly okay. Starting with consistent walks with your mom and exploring the possibility of visiting the gym is already a positive step forward. On a scale of 0 to 10, how confident are you in doing these actions in the following 7 days?\n\nUser: 7 probably.\n\nBot: A 7 is a solid level of confidence, which indicates that you feel fairly positive about these actions. Remember that every bit of activity counts, and starting with manageable goals is a great way to build consistency. I’ll follow up with you around this time every two days to check in and see how things are going. Do you feel ready to take these small steps forward?\n\nUser: Yes small steps is important sometimes.\n\nBot: Absolutely, small steps can lead to significant progress over time. It\'s wonderful to hear that you\'re ready to take those steps. I\'m excited to check in with you soon to hear how it\'s going. Remember, every bit of activity counts and contributes to your goals. Thank you for sharing with me today!\n\nUser: No problem!\n\nBot: Great! If you have any questions or need support along the way, feel free to reach out. I\'m here to help. Take care, and I\'ll talk to you again soon!\n\nUser: Thanks. Are you supposed to send me a second session.\n\nBot: Yes, I\'ll be following up with you around this time every two days. That way, we can see how things are going and make any adjustments if needed. Looking forward to our next session!",
    participant_id: "whatsapp:+18628813389",
    session: "session_1",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_24': {
    text: "Bot: Hi there! 🌟 How are the stretches and walks going? Remember, small steps count! Maybe set a reminder to stand and stretch if you’ve been sitting for a while. 🚶‍♀️ Let me know how you\'re doing! 😊\n\nUser: Ok\n\nBot: How have the past two days been for you? Were you able to fit in any physical activity, like the stretches or walks we talked about? 😊\n\nUser: Yes. I have noticed my muscles are a little sorer\n\nBot: I understand that soreness can be a bit uncomfortable, but it often means your muscles are getting stronger. How did you feel emotionally while doing the activities? Did it have any impact on your mood or stress levels?\n\nUser: But not as stiff\n\nBot: That\'s great to hear that you\'re feeling less stiff! It sounds like you\'re making some positive progress. How do you feel about continuing with these activities, or is there anything you\'d like to adjust in your plan?\n\nUser: I can keep up this pace. I would like to add swimming.\n\nBot: That\'s fantastic! Swimming is a great choice since it\'s easy on the joints and excellent for overall fitness. You\'re doing an amazing job by taking these steps to improve your well-being. How do you plan to fit swimming into your routine? 🏊‍♀️\n\nUser: I have a membership to a gym\n\nBot: That\'s great to hear! Having a gym membership gives you a convenient way to incorporate swimming into your routine. How often do you think you\'d like to swim each week? 🏊‍♂️\n\nUser: Before work 2 times a week\n\nBot: That sounds like a great plan! Swimming before work twice a week can be a refreshing way to start your day. How confident are you about making this a regular part of your routine?\n\nUser: 50%\n\nBot: It\'s completely normal to feel that way when starting something new. Would you like to explore some strategies together to help boost your confidence and make this plan more achievable?\n\nUser: It would be a big change in routine\n\nBot: I get that changing your routine can be a bit daunting. It\'s fantastic that you\'re committed to increasing your activity level. Maybe starting with small, manageable goals or setting reminders could help you ease into this new habit. What do you think?\n\nUser: Maybe after work would be better\n\nBot: Switching to after work sounds like a smart adjustment. It\'s important to find a time that fits well with your schedule. Would you like to go over your goals to make sure they align with this new plan?\n\nUser: Ok\n\nBot: It\'s great that you\'re thinking about what fits best into your schedule. With swimming after work twice a week, do you have specific days in mind that might help make it a consistent part of your routine?\n\nUser: Tuesday Thursday\n\nBot: Tuesday and Thursday sound like a solid plan. It\'s great that you\'re finding a routine that works for you. How do you feel about this new schedule? Does it seem manageable?\n\nUser: I think so\n\nBot: I\'m glad to hear that! Would you like to go over your goals to make sure everything fits well with your new schedule?\n\nUser: Yes\n\nBot: I appreciate your willingness to adjust your routine. It sounds like you\'re committed to making this work. With swimming on Tuesdays and Thursdays after work, how do you see this fitting in with your current activities, like walking and stretching?\n\nUser: I think I can do it\n\nBot: That\'s great to hear! It sounds like you\'re setting yourself up for success with a balanced plan. Having a clear path forward can be really motivating. Is there anything else you\'d like to adjust or add to your action plan?\n\nUser: No\n\nBot: It seems like you\'re all set with a great plan. If you ever want to revisit your goals or need any support, feel free to reach out. You\'re doing an amazing job! Is there anything else you\'d like to discuss?\n\nUser: Not today\n\nBot: If you ever want to revisit your goals or need any support, feel free to reach out. You\'re doing an amazing job! Before we wrap up, how are you feeling today? Are you experiencing any stress or anything on your mind that you\'d like to talk about? 😊\n\nUser: Feel pretty focused\n\nBot: It\'s great that you\'re feeling focused! If you need a quick mood boost, watching funny animal videos can be a delightful way to relieve stress and enhance your day. Check out this link for some laughs: [Funny Animal Videos](https://www.youtube.com/results?search_query=funny+animal+videos). On a scale of 1 to 10, how helpful was this suggestion? Please also share how it made you feel or any other thoughts you have about it.\n\nUser: 3. I am not into that kind of thing\n\nBot: I appreciate your honesty! It’s important to find what works for you. If you ever want to explore other ways to relieve stress or boost your mood, just let me know. Remember, you have a solid plan with swimming, walking, and stretching, and I believe you can make it work! \n\nThank you for our conversation today, and I look forward to hearing about your progress next time. Take care and enjoy your focused day! 😊 Goodbye!",
    participant_id: "whatsapp:+16123868977",
    session: "current_session",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_25': {
    text: "User: Hi\n\nBot: Hi! It\'s so great to meet you. I\'m here to help you explore ways to add more physical activity into your day. How are you doing today?\n\nUser: I\'m doing well, thank you\n\nBot: I\'m glad to hear that! Before we move on, I\'d be interested in knowing more about you so I can provide more personalized suggestions later. Can I ask, how do you usually unwind after work?\n\nUser: I like to hang out with my boyfriend and have some good food\n\nBot: That sounds like a lovely way to relax and enjoy your time! What are some other things that make you happy or recharge you? For example, some people enjoy experiencing nature, reading a good book, listening to music, or spending time with friends.\n\nUser: I like reading a good book, as well as doing arts and crafts\n\nBot: Those are great hobbies that allow for creativity and relaxation. How would you describe the environment you are living in? Is it in a city, or do you live in a more rural area?\n\nUser: I live in a city but everything is a little spread out\n\nBot: Got it! That can influence how you incorporate physical activities into your daily routine. What do you think has been holding you back from being more active? For example, common barriers include lack of time, social support, motivation, energy, and financial resources. Other concerns might be neighborhood safety, family obligations, weather, or fear of injury.\n\nUser: I don\'t always have time and I can be not very motivated\n\nBot: Those are very common barriers, and you\'re definitely not alone in feeling that way. Do you think stress is a significant barrier to more physical activity for you as well?\n\nUser: Yes absolutely\n\nBot: Stress can certainly impact our energy and motivation levels. Let’s explore some ways to work around these barriers. Instead of setting aside a lot of extra time, how do you feel about finding small opportunities throughout your day to add steps? These could include taking a quick walk during your lunch break, pacing while you’re on a phone call, or parking a little farther away when running errands. These small steps add up without needing a big time commitment. What does your regular day look like, and can we find some potential opportunities within it?\n\nUser: I take a short walk to my office (10 mins), and I work at the office all day, and then I walk back home and unwint\n\nBot: It sounds like you already have a bit of walking incorporated into your day, which is a great start. Perhaps we could find opportunities to extend those walks a little. You might consider taking a brief walk during your lunch break or even doing a few laps around the office if you have a moment to stretch. How do you feel about giving those a try?\n\nUser: I may feel a little weird walking around the office\n\nBot: That\'s completely understandable. Sometimes it can feel a bit awkward at first, but perhaps starting small, like taking the stairs instead of the elevator if that\'s an option, could be a more discreet way to add movement. Would something like stretching at your desk be more comfortable, or perhaps adding a small walk during your commute, like a short detour on your way home?\n\nUser: Yeah stretching at my desk is cool, and I am okay with taking detours\n\nBot: That\'s great! Stretching at your desk can be a great way to break up the day and refresh yourself. Taking a short detour on your way home can also add a bit of activity and help clear your mind after a day at the office. What kinds of benefits do you think being more active might bring to your life? Feel free to ask me if you need some examples.\n\nUser: I think it can help me be healthier and more productive\n\nBot: Absolutely, being more active can definitely contribute to better health and increased productivity. On a scale of 0 to 10, how important are these benefits to you?\n\nUser: I think maybe 8\n\nBot: That\'s a pretty significant level of importance! Increased productivity and better health can really make a positive impact on your daily life. Now that we\'ve reviewed some ideas and the benefits that matter to you, what actions do you plan to give a try in the following 7 days to be more physically active? For example, we discussed stretching at your desk and taking a detour on your way home.\n\nUser: I plan to add a detour\n\nBot: That sounds like a solid plan. Adding a detour can be a refreshing change and a good way to sneak in some extra steps. On a scale of 0 to 10, how confident are you in your ability to incorporate this detour in the following 7 days?\n\nUser: 8\n\nBot: That\'s a fantastic level of confidence! It sounds like you\'re really ready to incorporate this change. I\'ll follow up with you around this time every two days to check in and see how it\'s going. If you need any support or have any questions, feel free to let me know. Good luck, and enjoy your walks!\n\nUser: Thank you\n\nBot: You\'re welcome! I\'m here to support you, so don\'t hesitate to reach out if you need anything. Have a wonderful day, and take care!",
    participant_id: "whatsapp:+14045280621",
    session: "session_1",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 2
    }
  },
  'conv_26': {
    text: "Bot: Hello. Checking in on your progress with scheduling social conversations and nature walks. How is your weekly routine shaping up?\n\nUser: Going on well, struggling to adjust\n\nBot: a) How have you been these past two days?\n\nUser: Doing great\n\nBot: b) How did your plan for physical activity go? Did you get a chance to schedule social conversations and nature walks?\n\nUser: Yes,\n\nBot: c) When you were doing the physical activity, how did you feel emotionally?\n\nUser: Relief\n\nBot: Understood. Would you like to update your action plan for physical activity in any way?\n\nUser: Not now\n\nBot: FINISHED.",
    participant_id: "whatsapp:+18325682108",
    session: "current_session",
    round: "round_3",
    llm_scores: {
      emotional_reactions: 0,
      explorations: 1,
      interpretations: 0,
      empathy: 0
    }
  },
  'conv_27': {
    text: "Bot: Hey there! 😊 Just checking in—how have those scenic walks been going? It\'s impressive how you\'ve been fitting them in despite your busy schedule. Keep it up! 💪 Remember, I\'m here if you need any tips or encouragement. 🌟\n\nUser: I have not been keeping up with the walks\n\nBot: I get that it can be tough to maintain a routine, especially when things get busy. How have the past couple of days been for you in general?\n\nUser: Busier than ever :/\n\nBot: It sounds like things have been really hectic for you lately. It\'s great that you\'re aware of how busy you\'ve been. Were you able to fit in any physical activity, like those scenic walks, despite the busyness?\n\nUser: I was able to stretch but that\'s about it\n\nBot: I completely understand—when life gets hectic, it can be tough to keep up with everything. It\'s great that you still managed to fit in some stretching! That shows your commitment to staying active, even in small ways. How did you feel emotionally while you were stretching?\n\nUser: I was still stressed\n\nBot: It\'s completely normal to feel stressed, especially with everything on your plate. It\'s commendable that you still took a moment to stretch, even if it didn\'t fully ease the stress. Sometimes, those small steps can make a difference. Would you like to adjust your action plan for physical activity to better fit your current schedule? We could explore some stress-relieving activities that might help.\n\nUser: No adjustments needed\n\nBot: Understood! It\'s great that you\'re committed to your current plan. If you ever want to revisit your goals or need any support, feel free to reach out. I\'m here to help you stay on track. Is there anything else you\'d like to talk about or any other way I can assist you right now?\n\nUser: No all good\n\nBot: I\'m glad to hear you\'re feeling good about your plan! Just checking in—how are you feeling overall? Are you still feeling stressed, or has anything changed? Remember, even small steps count, and your dedication is something to be proud of. If you ever need support or just want to chat, I\'m here for you. Take care!\n\nUser: I\'m still stressed\n\nBot: I\'m sorry to hear you\'re feeling stressed. Watching funny animal videos can be a quick and effective way to lift your spirits and lighten your mood. Check out some videos here: [Funny Animal Videos](https://www.youtube.com/results?search_query=funny+animal+videos). On a scale of 1 to 10, how helpful was this suggestion? Please also share how it made you feel or any other thoughts you have about it.\n\nUser: 2, okay but not very effective",
    participant_id: "whatsapp:+14045280621",
    session: "session_4",
    round: "round_1",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 2,
      interpretations: 1,
      empathy: 1
    }
  },
  'conv_28': {
    text: "Bot: Hi there! Just checking in to see how your walks during lunch and on weekends are going. Remember, every step counts! Let me know if you need any support or adjustments. 😊 Keep up the great work!\n\nUser: Hello there,  my walks were great\n\nBot: Great to hear that. How did you feel emotionally while you were walking?\n\nUser: I felt better with each step\n\nBot: That\'s good to know. Do you feel any changes are needed for your current plan?\n\nUser: No, I think this plan is great and I can stick with it\n\nBot: Understood. Continue with your current plan, and we\'ll follow up to keep track of your progress. FINISHED\n\nUser: Thank you for your help\n\nBot: You\'re welcome. If you need further assistance, feel free to reach out.\n\nUser: I will\n\nBot: Great. Take care.",
    participant_id: "whatsapp:+17573246398",
    session: "current_session",
    round: "round_2",
    llm_scores: {
      emotional_reactions: 1,
      explorations: 1,
      interpretations: 1,
      empathy: 1
    }
  }
};
