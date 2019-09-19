# An adverbial case marker -(u)lo in Korean

A training set was created in the following ways. First, two small scale seed corpora were created manually in accordance to the two functions of (u)lo: directional and instrumental. Each by function corpus consisted of 100 instances with noun--(u)lo verb combinations. Since the same noun or verb can be attested in both the two functions in real life (see examples (1a b) and (2a b) above), we manipulated the degree of overlap across the two corpora such that 25 instances shared the same noun and another 25 instances shared the same verb. All instances were normed by two native speakers of Korean for the naturalness of each instance with respect to the functions where it belonged. Second, each noun and verb in these corpora was assigned to designated features. On top of a baseline corpus, four experimental corpora were created by manipulating feature weighting (noun target or verb target). This process yielded five separate corpora (i.e., baseline, noun target directional / instrumental, verb target directional / instrumental) which consisted of 100 instances of word feature combinations.

<ul>
  <li>
  (1a) -(u)lo as directional determined by a noun
    <ul>
      tolo lo ka ass ta
      </br>road DIR go PST SE1
      </br>‘(I) went to the road.’
    </ul>
  </li>
 
  <li>
  (1b) -(u)lo as instrumental determined by a noun
    <ul>
      cacenke lo ka ass ta
      </br>bicycle INS use PST SE
      </br>‘(I) went by bicycle.’
    </ul>
  </li>
  
  <li>
  (2a) -(u)lo as directional determined by a verb
    <ul>
      changko lo ka ass ta
      </br>warehouse DIR go PST SE
      </br>‘(I) went to the warehouse.’
    </ul>
  </li>
 
  <li>
  (2b) -(u)lo as instrumental determined by a verb
    <ul>
      changko lo ssu ess ta
      </br>warehouse INS use PST SE
      </br>‘(I) used (this) as a warehouse.’
    </ul>
  </li>
</ul>

## Baseline corpus:
As in (3), both nouns and verbs were paired with one basic feature corresponding to each word category (‘entity’ for a noun; ‘action’ for a verb).

<ul>
  <li>
  (3) Baseline
    <ul>
      {warehouse : ‘entity’} + (u)lo + {go : ‘action’}
    </ul>
  </li>
</ul>


##  Experimental corpora: 
In the noun target (4a b) or verb target (5a b) conditions, the target cue was paired with two features, one about the basic feature and the other about the specific feature of the target word category, whereas the non target cue was paired only with the basic feature.

<ul>
  <li>
  (4a) Noun target: directional
    <ul>
      {warehouse : ‘entity’ & ‘goal’} + (u)lo + {go : ‘action’}
    </ul>
  </li>
  <li>
  (4b) Noun target: instrumental
    <ul>
      {warehouse : ‘entity’ & ‘instrument’} + (u)lo + {go : ‘action’}
    </ul>
  </li>
  <li>
  (5a) Verb target: directional
    <ul>
      {warehouse: ‘entity’} + (u)lo + {go : ‘action’ & ‘movement’}
    </ul>
  </li>
  <li>
  (5b) Verb target: instrumental
    <ul>
      {warehouse: ‘entity’} + (u)lo + {go : ‘action’ & ‘use’}
    </ul>
  </li>
</ul>

Finally, a training set for each condition was created by repeating extraction of the instances of directional and instrumental randomly from the designated corpora. The sampling occurred from one to 30, yielding input corpora whose number of instances was from 100 to 3000, respectively. Frequency of occurrence that each function was attested (balanced frequency and skewed frequency) was manipulated at each sampling. In the balanced frequency condition, the two functions of -(u)lo were included at the same proportion; in the skewed frequency condition, the number of instances of instrumental was bigger than that of directional. A small number of non directional and non instrumental instances was also added to every training set in order to provide a noise in the course of learning (which mocks up the natural environment where learning occurs). Table 1 summarises the information about each training set by condition.

|  | Balanced frequency | Skewed frequency |
| --- | --- | --- |
| **Noun-target** | 49 directional </br>- 2 feature for noun </br>- 1 feature for verb </br>49 instrumental </br>- 2 feature for noun </br>- 1 feature for verb </br>2 noise | 39 directional </br>- 2 feature for noun </br>- 1 feature for verb </br>59 instrumental </br>- 2 feature for noun </br>- 1 feature for verb </br>2 noise |
| **Verb-target** | 49 directional </br>- 1 feature for noun </br>- 2 feature for verb </br>49 instrumental </br>- 1 feature for noun </br>- 2 feature for verb </br>2 noise | 39 directional </br>- 1 feature for noun </br>- 2 feature for verb </br>59 instrumental </br>- 1 feature for noun </br>- 2 feature for verb </br>2 noise|

<p style="text-align:center;">Table 1: Information about input by condition. Each number of directional, instrumental, and noise represents the proportion (not the actual number) of instances in a single corpus.</p>
