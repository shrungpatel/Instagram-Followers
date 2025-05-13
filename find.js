function uploadFiles() {
  const file1 = document.getElementById('followers').files[0];
  const file2 = document.getElementById('following').files[0];

  if (!file1 || !file2) {
    alert("Please select both files!");
    return;
  }

  const reader1 = new FileReader();
  const reader2 = new FileReader();

  try {
    reader1.onload = function(event) {
      try {
        const followersData = JSON.parse(event.target.result);
        reader2.onload = function(event) {
        try {
            const followingData = JSON.parse(event.target.result);
            const followingSet = new Set(
              followingData.relationships_following.map(person => person.string_list_data[0].value)
            );
            const followersSet = new Set(
              followersData.map(person => person.string_list_data[0].value)
            );
            const difference = [...followingSet].filter(value => !followersSet.has(value));
            document.getElementById('result').textContent = difference.join("\n");
          }
          catch (error) {
            alert("Error parsing the 'following' file.");
            console.error("Error parsing following file:", error);
          }
        };
        reader2.readAsText(file2);
      }
      catch (error) {
        alert("Error parsing the followers file.");
      }
    };
    reader1.readAsText(file1);
  }
  catch (error) {
    alert("Error! Please make sure you are uploading the right files");
  }
}