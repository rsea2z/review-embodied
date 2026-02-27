#!/bin/bash

# Initialize counters
vla_count=0
world_count=0
driving_count=0
manip_count=0
survey_count=0
rl_count=0

while IFS= read -r line; do
  case "$line" in
    *[Vv][Ll][Aa]*) ((vla_count++)) ;;
    *[Ww]orld*[Mm]odel*) ((world_count++)) ;;
    *[Dd]riving*|*[Vv]ehicle*) ((driving_count++)) ;;
    *[Mm]anipulation*|*[Gg]rasping*) ((manip_count++)) ;;
    *[Ss]urvey*|*[Rr]eview*) ((survey_count++)) ;;
    *[Rr]einforcement*|*[Pp]olicy*) ((rl_count++)) ;;
  esac
done < references-full.bib

echo "VLA Papers: $vla_count"
echo "World Model Papers: $world_count"
echo "Driving Papers: $driving_count"
echo "Manipulation Papers: $manip_count"
echo "Survey/Review Papers: $survey_count"
echo "RL Papers: $rl_count"
