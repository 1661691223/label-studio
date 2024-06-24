---
title: Generate predictions from a prompt
short: Generate predictions from a prompt
tier: enterprise
type: guide
order: 0
order_enterprise: 234
meta_title: Generate predictions
meta_description: Generate predictions to auto-label project tasks
section: Prompts
date: 2024-06-13 21:54:22
---

You can continue to save and evaluate your prompts until you reach your desired level of accuracy. When your prompt is ready, you can use it to generate predictions for all tasks within your project. 

!!! note
    Each time you click **Evaluate**, you generate a prediction for the tasks with ground truth annotation. Because you can have multiple models connected to the same project, this might result in multiple predictions for tasks. 


## Generate predictions for all tasks

When you are confident in your prompt, click **Get Predictions for All Tasks**. This may take some time to complete depending on how many tasks you have in your project. 

<video src="../images/prompts/predictions.mp4" controls="controls" style="max-width: 800px;" class="gif-border" />

!!! note 
    Predictions are not cumulative when using this action. If you get predictions for all tasks, change the prompt, and then generate predictions for all tasks again, you will overwrite your previous predictions and each task will only reflect the most recent prediction. 

Once complete, you can return to the project and open the Data Manager. Use the **Total predictions per task** column to confirm that each task has at least one prediction:

![Screenshot of the prediction preview](/images/prompts/prediction_column.png)

## Remove predictions

If you prematurely generated predictions or want to use a new prompt, simply select all tasks and select **Actions > Delete Predictions**. To only remove predictions from certain models or model versions, use the **Predictions** page in the project settings. 

## Create annotations from predictions

Once you have your predictions in place, you still need to convert them to annotations. You can review predictions by opening tasks. The predictions are listed under the model name and are grayed out: 

![Screenshot of the prediction preview](/images/prompts/prediction.png)


From the Data Manager, select all the tasks you want to label and then select **Actions > Create Annotations from Predictions**. You are asked to select the model and version you want to use. 

![Gif of the of create annotations action](/images/prompts/create_annotations_1.png)