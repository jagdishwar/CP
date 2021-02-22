#include<bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define start_routine() int begtime = clock();
#define end_routine() int endtime = clock(); \
                      cerr << "\n\n" << "Time elapsed: " << \
                      (endtime - begtime)*1000/CLOCKS_PER_SEC << " ms\n\n"; \
                      return 0;
#define ll long long int
#define ull unsigned long long int
#define db long double
#define ff first
#define ss second
#define MP make_pair
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define pii pair<int , int>
#define pdd pair<db , db>
#define pll pair<ll , ll
#define vpl vector<pll >
#define spl set<pll >
#define vll vector<ll >
#define mod 1000000007
#define mod1 998244353
#define inf 1000000000000000007
#define eps 0.000001
#define stp fixed<<setprecision(20)
#define endl '\n'
#define codejam 0



int main()
{
 ll n;cin>>n;
    ll last[n+1];
    for(ll i=0;i<=n;i++)
        last[i]=0;
    string s;cin>>s;

    s='*'+s;

    vector<string> ans;
    for(ll i=1;i<=n;i++)
    {
        set<char> occ;
        string s1="";
        ll j;
        for(j=i;j<=n;j++)
        {
            if(occ.size() && occ.find(s[j])!=occ.end())
            {
                last[i]=j-1;
                if(i==1)
                {
                    ans.pb(s1);
                    break;
                }
                else
                {
                    if(s[j]==s[i])
                        break;
                    if(j-1>last[i-1])
                    {
                        ans.pb(s1);
                        break;
                    }
                }
            }
            else
            {
                occ.insert(s[j]);
                s1+=s[j];
            }
        }
        if(j==n+1)
        {
            ans.pb(s1);
            break;
        }
    }
    sort(ans.begin(), ans.end());
    for(auto i:ans)
        cout<<i<<" ";

}