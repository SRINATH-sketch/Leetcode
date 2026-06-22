void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n)
{
    int c=0,j=0;
    for(int i=0;i<m;i++)
    {
        nums1[c]=nums1[i];
        c+=1;
    }
    for(int i=0;i<n;i++)
    {
        nums1[c]=nums2[i];
        if(c<n+m)
        {
            c+=1;
        }
    }
    int temp;
    for(int i=0;i<c-1;i++)
    {
        for(int j=0;j<c-i-1;j++)
        {
            if(nums1[j]>nums1[j+1])
            {
                temp=nums1[j];
                nums1[j]=nums1[j+1];
                nums1[j+1]=temp;
            }
        }
    }
}