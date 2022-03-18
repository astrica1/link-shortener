echo "Push to github remote"
echo $(git push origin --all)
echo $(git push origin --tags)
echo "Push to github remote done"
echo
echo "Push to gitlab remote"
echo $(git push alter --all)
echo $(git push alter --tags)
echo "Push to gitlab remote done"