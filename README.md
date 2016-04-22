# Live Streaming of Brain Sensing Data

## Motivation
Post Traumatic Stress Disorder (PTSD) causes veterans a plethora of problems in reintegrating with their normal lives. While various treatment modalities exist, the central principle underpinning most of the them is the ability to maintain awareness. One of the challenges with PTSD is the zone-out that occurs, where the veteran loses focus and is unable to concentrate on his or her job. This project uses live data from a brain sensing headband to gently cue the veteran when he or she zones out.

## Methodology
A 3 step methodology is involved:

1. Training Data Acquistion: The veteran puts on the headband and plays some games that provide data on their unique brainwave signature of attention vs inattention.
2. Classifier Training: The training data is then mined for patterns using an SVM algorithm
3. Deployment: As proof of concept, a live streaming visualization is displayed in this case. In actual use cases, either a mobile phone or wearable would gently cue the user and help them get back to an attentive state
