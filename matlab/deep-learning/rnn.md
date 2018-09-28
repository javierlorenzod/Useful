## Helpful function (NLP: Natural Language Processing)

This function calculates the dummy variable for some text. This is useful in order to train a network with non-numerical data in which the distance between possible inputs is not relevant and could confuse the network, giving more weight to certain inputs.
```matlab
function m = dummifyText(t)
    vocab = uint8([newline char(13) ' !"&''(),-.01234678:;?ABCDEFGHIJKLMNOPQRSTUVWY[]_`abcdefghijklmnopqrstuvwxyz']);
    m = dummyvar(categorical(uint8(t),vocab)')';
end
```
